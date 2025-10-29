from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt
from ..models import db, Doctor
from ..api1 import cache

class DoctorApi(Resource):
    #read
    @jwt_required()
    @cache.cached(timeout=300)
    def get(self):
        # Get optional query param for department
        department_id = request.args.get('department_id', type=int)

        query = Doctor.query

        # Filter by department if provided
        if department_id:
            query = query.filter_by(department_id=department_id)

        doctors = query.all()

        if not doctors:
            return {'message': 'No doctors found for this department'}, 404

        # Return list of doctors
        return [d.convert_to_json() for d in doctors], 200
    
    
    #create
    @jwt_required()
    def post(self):
        current_user=get_jwt()
        if current_user.get('role') != 'admin':
            return {'message': 'Access denied!'}, 403
        
        data=request.get_json()
        if not (data.get('name') and data.get('email') and data.get('password') and data.get('department_id')):
            return {'message' : 'Bad request! all the data fields are required.'}, 400
        
        if len(data.get('name').strip()) > 50 or len(data.get('name').strip()) < 3 :
            return {'message' : 'Name should be in between 3-50 characters long'}
        
        if len(data.get('email').strip()) > 60 or "@" not in data.get('email') :
            return {'message' : 'email should contain @ and should be in less than 60 character'}
        
        if len(data.get('password').strip()) > 20 or len(data.get('password').strip()) < 6 :
            return {'message' : 'password should be in between 6-20 charcters long'}

        doctor=Doctor.query.filter_by(email=data.get('email')).first()
        if doctor:
            return {'message' : 'Doctor already exists.'}, 400
        
        new_doctor=Doctor(name=data.get('name').strip(), email=data.get('email').strip(), password=data.get('password').strip(),
                           department_id = data.get('department_id'),profile = data.get('profile'), contact=data.get('contact'), experience_years = data.get('experience_years'),
                           qualification = data.get('qualification'), about = data.get('about'))
        db.session.add(new_doctor)
        db.session.commit()
        return {'message' : 'Doctor registered successfully'}, 201     

    # update 
    @jwt_required()
    def put(self, doctor_id):
        current_user=get_jwt()
        if current_user.get('role') != 'admin':
            return {'message': 'Access denied!'}, 403
        
        data=request.get_json()
        if not (data.get('name') and data.get('email') and data.get('password')):
            return {'message' : 'Bad request! all the data fields are required.'}, 400
        
        if len(data.get('name').strip()) > 50 or len(data.get('name').strip()) < 3 :
            return {'message' : 'Name should be in between 3-50 characters long'}
        
        if len(data.get('email').strip()) > 60 or "@" not in data.get('email') :
            return {'message' : 'email should contain @ and should be in less than 60 character'}
        
        if len(data.get('password').strip()) > 20 or len(data.get('password').strip()) < 6 :
            return {'message' : 'password should be in between 6-20 charcters long'}

        doctor=Doctor.query.get(doctor_id)
        if  not doctor:
            return {'message' : 'Doctor not found.'}, 404
        
        doctor.name=data.get('name').strip()
        doctor.email=data.get('email').strip()
        doctor.password=data.get('password').strip()
        doctor.department_id=data.get('department_id')
        doctor.profile=data.get('profile').strip()
        doctor.contact=data.get('contact').strip()
        doctor.experience_years=data.get('experience_years')
        doctor.qualification=data.get('qualification').strip()
        doctor.about=data.get('about').strip()
        db.session.commit()
        return {'message' : 'Doctor details updated successfully'}, 200    
     
     #delete
    @jwt_required()
    def delete(self, doctor_id):
        current_user=get_jwt()
        if current_user.get('role') != 'admin':
            return {'message': 'Access denied!'}, 403
        
        doctor=Doctor.query.get(doctor_id)
        if  not doctor:
            return {'message' : 'Doctor not found.'}, 404
        
        db.session.delete(doctor)
        db.session.commit()
        return {'message' : 'Doctor deleted successfully'}, 200  