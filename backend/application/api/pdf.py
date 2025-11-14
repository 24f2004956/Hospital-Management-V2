from flask import send_file, request, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from io import BytesIO
from datetime import datetime
from sqlalchemy import extract
from ..models import Appointment


class PDFReportAPI(Resource):

    @jwt_required()
    def get(self):
        current_user = get_jwt()
        if current_user.get("role") != "admin":
            return {"message": "Access Denied"}, 403

        month = request.args.get('month')  #  YYYY-MM
        if not month:
            return {"message": "Month parameter is required. Example: ?month=2025-01"}, 400

        year, month_num = map(int, month.split("-"))

        appointments = Appointment.query.filter(
            extract('year', Appointment.date) == year,
            extract('month', Appointment.date) == month_num,
            Appointment.status != "Cancelled"
        ).all()

        buffer = BytesIO()
        pdf = canvas.Canvas(buffer, pagesize=A4)
        pdf.setTitle(f"Monthly Activity Report - {month}")

        pdf.setFont("Helvetica-Bold", 16)
        pdf.drawString(50, 800, f"Monthly Activity Report: {month}")

        pdf.setFont("Helvetica", 12)
        y = 760

        if not appointments:
            pdf.drawString(50, y, "No appointments recorded this month.")
        else:
            for idx, a in enumerate(appointments, start=1):

                patient_name = a.user.name if a.user else "Unknown"
                department_name = a.doctor.department.name if a.doctor and a.doctor.department else "N/A"
                doctor_name = a.doctor.name if a.doctor else "Unknown"

                text = (
                    f"{idx}. {patient_name} | Department: {department_name} | "
                    f"Doctor: {doctor_name} | Date: {a.date.strftime('%Y-%m-%d')}"
                )

                pdf.drawString(50, y, text)
                y -= 18

                if y < 50:
                    pdf.showPage()
                    pdf.setFont("Helvetica", 12)
                    y = 800

        pdf.save()
        buffer.seek(0)

        return send_file(
            buffer,
            as_attachment=True,
            download_name=f"Monthly_Report_{month}.pdf",
            mimetype="application/pdf"
        )
