from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt
from ..models import db, User, Appointment, Doctor
from ..api1 import cache

class PatientApi(Resource):

    @jwt_required()
    @cache.cached(timeout=60)
    def get(self):
        current_user = get_jwt()
        role = current_user.get('role')
        
        if role == "doctor":
            doctor_id = int(current_user.get('sub'))

            appointments = Appointment.query.filter_by(doctor_id=doctor_id).all()
            patient_ids = {appt.patient_id for appt in appointments}

            patients = User.query.filter(User.id.in_(patient_ids)).all()
            return [p.convert_to_json() for p in patients], 200

        if role == "admin":
            patients = User.query.filter_by(role="patient").all()
            return [p.convert_to_json() for p in patients], 200
        
        if role == 'patient':
            user_id = int(current_user.get('sub'))
            patient = User.query.get(user_id)
            return patient.convert_to_json(), 200

        return {"message": "Unauthorized"}, 403


    
   

    @jwt_required()
    def put(self, patient_id):
        current_user=get_jwt()
        if current_user.get('role') != 'admin':
            return {'message': 'Access denied!'}, 403
        
        data=request.get_json()
        if not (data.get('name') and data.get('email') ):
            return {'message' : 'Bad request! all the data fields are required.'}, 400
        
        if len(data.get('name').strip()) > 50 or len(data.get('name').strip()) < 3 :
            return {'message' : 'Name should be in between 3-50 characters long'}
        
        if len(data.get('email').strip()) > 60 or "@" not in data.get('email') :
            return {'message' : 'email should contain @ and should be in less than 60 character'}

        patient = User.query.filter_by(id=patient_id, role="patient").first()
        if  not patient:
            return {'message' : 'Patient not found.'}, 404
        
        patient.name=data.get('name').strip()
        patient.email=data.get('email').strip()
        patient.profile=data.get('profile')
        patient.contact=data.get('contact')
        patient.age=data.get('age')
        patient.gender=data.get('gender')
        patient.address=data.get('address')
        db.session.commit()
        return {'message' : 'Patient details updated successfully'}, 200    
     
 
    @jwt_required()
    def delete(self, patient_id):
        current_user=get_jwt()
        if current_user.get('role') != 'admin':
            return {'message': 'Access denied!'}, 403
        
        patient=User.query.get(patient_id)
        if  not patient:
            return {'message' : 'Patient not found.'}, 404
        
        db.session.delete(patient)
        db.session.commit()
        return {'message' : 'Patient deleted successfully'}, 200  
    
class PatientProfileUpdateAPI(Resource):
        
    @jwt_required()
    def put(self):
        current_user = get_jwt()
        
        
        if current_user.get('role') != 'patient':
            return {"message": "Access denied!"}, 403
        
        user_id = int(current_user.get('sub'))
        data = request.get_json()

        patient = User.query.filter_by(id=user_id, role="patient").first()
        if not patient:
            return {"message": "Patient not found"}, 404

       
        if "name" in data:
            if len(data["name"].strip()) < 3 or len(data["name"].strip()) > 50:
                return {"message": "Name should be 3-50 chars long"}, 400
            patient.name = data["name"].strip()

        
        if "email" in data:
            if "@" not in data["email"] or len(data["email"]) > 60:
                return {"message": "Invalid email format"}, 400
            patient.email = data["email"].strip()

       
        patient.age = data.get("age", patient.age)
        patient.gender = data.get("gender", patient.gender)
        patient.address = data.get("address", patient.address)
        patient.contact = data.get("contact", patient.contact)
        patient.profile = data.get("profile", patient.profile)

        db.session.commit()
        return {"message": "Profile updated successfully"}, 200


