from .worker import celery , app
from celery.schedules import crontab
from .models import User,Doctor, Appointment
from jinja2 import Template
from datetime import date, timedelta
from sqlalchemy import extract
import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.mime.multipart import MIMEMultipart
import csv
import os


def send_mail(email, subject, email_content, attachment=None):
    # Define email server and credentials
    smtp_server_host = "localhost"
    smtp_port = 1025
    sender_email = "admin@gmail.com"
    sender_password = "123456"
     
      # Create the email message
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = email
    msg["Subject"] = subject

    # Attach the HTML content to the email
    msg.attach(MIMEText(email_content, "html"))

    if attachment:
        with open(attachment, "rb") as attachment_content:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment_content.read())
            encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % os.path.basename(attachment))
        msg.attach(part)

    # Set up email server
    server = smtplib.SMTP(host=smtp_server_host, port=smtp_port)
    server.login(sender_email, sender_password)
    server.send_message(msg)
    server.quit()
    print('mail sent')

    
@celery.on_after_configure.connect
def setup_periodic_task(sender, **kwargs):
    # sender.add_periodic_task(10.0, monthly_report.s(), name='monthly report sent at 10sec')
    # sender.add_periodic_task(5.0, daily_reminder.s(), name='daily_reminder sent successfully')

    sender.add_periodic_task(
        crontab(hour=9, minute=0),
        daily_reminder.s(),
        name = 'daily_remainder at 9:00 a.m'
    )

    sender.add_periodic_task(
        crontab(day_of_month='1', month_of_year='*'),
        monthly_report.s(),
        name = 'monthly_report at 1st of every month'
    )


@celery.task
def daily_reminder():
    with app.app_context():
        appointments = Appointment.query.filter_by(date=date.today())

        for appointment in appointments:
            patient = User.query.get(appointment.patient_id)
            doctor = Doctor.query.get(appointment.doctor_id)

            if patient and patient.email:
                message = f"""
                Hello {patient.name},

                This is a reminder that you have an appointment TODAY with Dr. {doctor.name}.
                Time: {appointment.time.strftime('%I:%M %p')}

                Please make sure to reach the hospital on time.
                """

                send_mail(email=patient.email, email_content=message, subject="Hospital Visit Remainder")

                print(f"Reminder sent to {patient.name}")
    
@celery.task
def monthly_report():
    with app.app_context():
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        template_path = os.path.join(BASE_DIR, "report.html") 


        today = date.today()
        first_day_current_month = today.replace(day=1)
        last_day_prev_month = first_day_current_month - timedelta(days=1)
        month = last_day_prev_month.month
        year = last_day_prev_month.year

        doctors = Doctor.query.all()

        for doctor in doctors:
            appointments = (
                Appointment.query
                .filter_by(doctor_id=doctor.id)
                .filter(extract('month', Appointment.date)==month)
                .filter(extract('year', Appointment.date)==year)
                .all()
            )

            if not appointments:
                continue  


            with open(template_path, "r") as file:
                jinja_template = Template(file.read())
                html_report=jinja_template.render(doctor=doctor,
                            appointments=appointments,
                            month_name=last_day_prev_month.strftime("%B"),
                            year=year,)

            send_mail(email=doctor.email, email_content=html_report, subject="Monthly Report")

            print(f"Monthly report sent to Dr. {doctor.name}")   

@celery.task
def data_export(treatment_details, email): #treatmeant_details => list of dictonaries => [{..},{..},{..}...]
    with open('data_export.csv', 'w', newline='') as  csvfile:
        fieldnames = ["name","doctor_name","diagnosis","prescription","notes","upcoming_visit","visit_type","test_done","medicines"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(treatment_details)

    send_mail(email=email, email_content="Please find the exported data.", subject="Treatment Data Export", attachment="data_export.csv")    
    return "Data Exported!!"



    