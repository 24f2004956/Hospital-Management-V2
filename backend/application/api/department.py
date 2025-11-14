from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt
from ..models import db, Doctor, Department
from ..api1 import cache

class DepartmentApi(Resource):

    @jwt_required()
    def get(self, department_id=None):

       
        if department_id:
            department = Department.query.get(department_id)
            if not department:
                return {"message": "Department not found"}, 404
            return department.convert_to_json(), 200

       
        departments = Department.query.all()
        return [dept.convert_to_json() for dept in departments], 200
    
 
    @jwt_required()
    def post(self):
        current_user=get_jwt()
        if current_user.get('role') != 'admin':
            return {'message': 'Access denied!'}, 403
        
        data=request.get_json()
        if not (data.get('name') and data.get('description')):
            return {'message' : 'Bad request! all the data fields are required.'}, 400
        
        if len(data.get('name').strip()) > 50 or len(data.get('name').strip()) < 3 :
            return {'message' : 'Name should be in between 3-50 characters long'}
        
        
        if len(data.get('description').strip()) > 150 or len(data.get('description').strip()) < 10 :
            return {'message' : 'description should be in between 10-150 characters long'}

        department=Department.query.filter_by(name=data.get('name')).first()
        if department:
            return {'message' : 'Department already exists.'}, 400
        
        new_department=Department(name=data.get('name').strip(), description=data.get('description').strip())
        db.session.add(new_department)
        db.session.commit()
        return {'message' : 'Department added successfully'}, 201     


    @jwt_required()
    def put(self, department_id):
        current_user=get_jwt()
        if current_user.get('role') != 'admin':
            return {'message': 'Access denied!'}, 403
        
        data=request.get_json()
        if not (data.get('name') and data.get('description')):
            return {'message' : 'Bad request! all the data fields are required.'}, 400
        
        if len(data.get('name').strip()) > 50 or len(data.get('name').strip()) < 3 :
            return {'message' : 'Name should be in between 3-50 characters long'}
        
        if len(data.get('description').strip()) > 150 or len(data.get('description').strip()) < 10 :
            return {'message' : 'password should be in between 10-150 characters long'}

        department=Department.query.get(department_id)
        if  not department:
            return {'message' : 'Department not found.'}, 404
        
        department.name=data.get('name').strip() if data.get('name').strip() else department.name 
        department.description=data.get('description').strip()
        db.session.commit()
        return {'message' : 'Department details updated successfully'}, 200    
     

    @jwt_required()
    def delete(self, department_id):
        current_user=get_jwt()
        if current_user.get('role') != 'admin':
            return {'message': 'Access denied!'}, 403
        
        department=Department.query.get(department_id)
        if  not department:
            return {'message' : 'Department not found.'}, 404
        
        db.session.delete(department)
        db.session.commit()
        return {'message' : 'Department deleted successfully'}, 200  