from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column ,Integer, String, ForeignKey, Date, Time
from datetime import datetime
 
db=SQLAlchemy()

class User(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(20), nullable=False)
    role = Column(String(20), nullable=False, default="patient") # patient, doctor, admin(hospital staff)
    black_list_status = Column(String(20), nullable=False, default="deactive" ) # deactive, active(blacklisted)
    profile = Column(String(200))
    contact = Column(String(15))
    age = Column(Integer)
    gender = Column(String(10))
    address = Column(String(120))

    appointment = db.relationship('Appointment', backref='user')
  

    def convert_to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "role": self.role,
            "profile": self.profile,
            "age": self.age,
            "gender": self.gender,
            "address": self.address,
        }

class Doctor(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(60), unique=True, nullable=False)
    password = Column(String(20), nullable=False)
    role = Column(String(20), nullable=False, default="doctor") # patient, doctor, admin(hospital staff)
    black_list_status=Column(String(20), nullable=False, default="deactive" ) # deactive, active(blacklisted)
    department_id = Column(Integer, ForeignKey('department.id'), nullable=False)
    contact = Column(String(15))
    profile = Column(String(200))
    experience_years = Column(Integer) 
    qualification = Column(String(50))
    about = Column(String(150))
    
    appointment = db.relationship('Appointment', backref='doctor')


    def convert_to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "department_id": self.department_id,
            "profile": self.profile, 
            "contact": self.contact,
            "experience_years": self.experience_years,
            "qualification": self.qualification,
            "about": self.about,
            "department_id": self.department_id,
        }

class DoctorAvailability(db.Model):
    id = Column(Integer, primary_key=True)
    doctor_id = Column(Integer, ForeignKey('doctor.id'), nullable=False)
    date = Column(Date, nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    status = Column(String(20), default='available')  # available  booked  unavailable

    def convert_to_json(self):
        return {
            "id": self.id,
            "doctor_id": self.doctor_id,
            "date": str(self.date),
            "start_time": str(self.start_time),
            "end_time": str(self.end_time),
            "status": self.status
        }    

class Department(db.Model):
    id = Column(Integer, primary_key=True)
    doctor = db.relationship('Doctor', backref='department')
    name = Column(String(50), nullable=False)
    description = Column(String(120),  nullable=False)

    def convert_to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
        }

class Appointment(db.Model):
    id = Column(Integer, primary_key=True)
    doctor_id = Column(Integer, ForeignKey('doctor.id'), nullable=False)
    patient_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    date = Column(Date, nullable=False, default=datetime.utcnow)
    time = Column(Time, nullable=True)
    status = Column(String(20),nullable=False,default='Booked') # Booked ,Completed, Cancelled
    reason = Column(String(150))
    treatment = db.relationship('Treatment', backref='appointment')

    def convert_to_json(self):
        return {
            "id": self.id,
            "doctor_id": self.doctor_id,
            "patient_id": self.patient_id,
            "date": self.date.strftime("%Y-%m-%d"),   #strftime 
            "time": self.time.strftime("%I:%M %p"),
            "status": self.status,
            "reason": self.reason
        }

class Treatment(db.Model):
    id = Column(Integer, primary_key=True)
    appointment_id = Column(Integer, ForeignKey('appointment.id'), nullable=False)
    diagnosis = Column(String(100), nullable=False)
    prescription = Column(String(200), nullable=False)
    notes = Column(String(200))
    visit_type = Column(String(50))
    test_done = Column(String(100))
    medicines = Column(String(200))

    def convert_to_json(self):
        return {
            "id": self.id,
            "appointment_id": self.appointment_id,
            "diagnosis": self.diagnosis,
            "prescription": self.prescription,
            "notes": self.notes,
            "visit_type": self.visit_type,
            "test_done": self.test_done,
            "medicines": self.medicines
        }
