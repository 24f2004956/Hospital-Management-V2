from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column ,Integer, String, ForeignKey
from datetime import datetime
 
db=SQLAlchemy()

class User(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(20), nullable=False)
    role = Column(String(20), nullable=False, default="patient") # patient, doctor, admin(hospital staff)
    black_list_status = Column(String(20), nullable=False, default="deactive" ) # deactive, activate(blacklisted)
    profile = Column(String())
    contact = Column(String(15))
    appointment = db.relationship('Appointment', backref='user')

class Doctor(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(60), unique=True, nullable=False)
    password = Column(String(20), nullable=False)
    role = Column(String(20), nullable=False, default="doctor") # patient, doctor, admin(hospital staff)
    black_list_status=Column(String(20), nullable=False, default="deactive" ) # deactive, activate(blacklisted)
    department = db.relationship('Department', backref='doctor')
    appointment = db.relationship('Appointment', backref='doctor')

class Department(db.Model):
    id = Column(Integer, primary_key=True)
    doctor_id = Column(Integer, ForeignKey('doctor.id'), nullable=False)
    name = Column(String(50), nullable=False)
    description = Column(String(120),  nullable=False)

class Appointment(db.Model):
    id = Column(Integer, primary_key=True)
    doctor_id = Column(Integer, ForeignKey('doctor.id'), nullable=False)
    patient_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    date = Column(String(20), default=datetime.now(), nullable=False)
    time = Column(String())
    status = Column(String(20),nullable=False,default='uncomplete') #complete, uncomplete
    treatment = db.relationship('Treatment', backref='appointment')

class Treatment(db.Model):  
    id = Column(Integer, primary_key=True)
    appointment_id = Column(Integer,ForeignKey('appointment.id'), nullable=False)
    diagnosis = Column(String(50),nullable=False)  
    prescription = Column(String(100),nullable=False)  
    notes = Column(String(100),nullable=True)  

class Patient_History(db.Model):
    id = Column(Integer, primary_key=True)
    visit_type = Column(String())
    test_done = Column(String()) 
    Diagonsis = Column(String())
    medicines = Column(String())
    prescription = Column(String())