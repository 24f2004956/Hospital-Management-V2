from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt
from ..models import db, Doctor, User

class PatientApi(Resource):
    #read
    @jwt_required()
    def get(self):
        patients = User.query.filter_by(role = "patient").all()
        print(patients)

        patient_json = []
        for patient in patients:
            patient_json.append(patient.convert_to_json())
        return patient_json, 200    
    
   
    # update 
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
        patient.password=data.get('password').strip()
        patient.profile=data.get('profile')
        patient.contact=data.get('contact')
        patient.age=data.get('age')
        patient.gender=data.get('gender')
        patient.address=data.get('address')
        db.session.commit()
        return {'message' : 'Patient details updated successfully'}, 200    
     
     #delete
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