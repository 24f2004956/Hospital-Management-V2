from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from ..models import db, User, Doctor
from ..api1 import cache


class LoginApi(Resource):
    def post(self):
        data=request.get_json()

        if not (data.get('email') and data.get('password')):
            return {'message' : 'Both email & password fields are required.'}, 400
        
        user = User.query.filter_by(email=data.get('email')).first()
        doctor = Doctor.query.filter_by(email=data.get('email')).first()

        account= user or doctor

        if not account:
            return {'message' : 'Account not found.'}, 404
        
        if account.password != data.get('password'):
            return {'message' : 'Incorrect password'}, 400
        
        if (account.black_list_status == 'active'):
            return {'message': 'Your account has been blacklisted'}, 400

        
        #token = create_access_token({'role' : user.role, 'user_id' : user.id})    # used in older version of jwt if used get the error " subject must be a string"
        token = create_access_token(
                                    identity=str(account.id),              # string for JWT "sub"
                                    additional_claims={"role": account.role}  # extra info
                                )
        
        return {
                'message': 'User logged in successfully.',
                'token' : token,
                'user_name' : account.name,
                'user_role' : account.role
                }, 200 ,
    
    @jwt_required()   
    def patch(self, account_type, account_id):

        current_user = get_jwt()

        if current_user.get('role') != 'admin':
            return {'message': 'Access denied!'}, 403

        if account_type == "patient":
            account = User.query.get(account_id)
        elif account_type == "doctor":
            account = Doctor.query.get(account_id)
        else:
            return {'message': 'Invalid account type.'}, 400

        if not account:
            return {'message': 'Account not found.'}, 404

        data = request.get_json()
        new_status = data.get('status', 'active')
        if new_status not in ['active', 'deactive']:
            return {'message': 'Invalid status.'}, 400

        account.black_list_status = new_status
        db.session.commit()

        return {'message': f'{account_type.capitalize()} account {("Blacklisted" if new_status=="active" else "Unblacklisted")} successfully.'}, 200
     


class RegisterApi(Resource):
    def post(self):
        data=request.get_json()
        if not (data.get('name') and data.get('email') and data.get('password')):
            return {'message' : 'Bad request! all the data fields are required.'}, 400
        
        if len(data.get('name').strip()) > 50 or len(data.get('name').strip()) < 3 :
            return {'message' : 'Name should be in between 3-50 characters long'}
        
        if len(data.get('email').strip()) > 60 or "@" not in data.get('email') :
            return {'message' : 'email should contain @ and should be in less than 60 character'}
        
        if len(data.get('password').strip()) > 20 or len(data.get('password').strip()) < 6 :
            return {'message' : 'password should be in between 6-20 charcters long'}

        user=User.query.filter_by(email=data.get('email')).first()
        if user:
            return {'message' : 'User already exists.'}, 400
        
        new_user=User(name=data.get('name').strip(), email=data.get('email').strip(), password=data.get('password').strip(), 
                      profile = data.get('profile'), contact = data.get('contact'), age = data.get('age'), gender = data.get('gender'), address = data.get('address') )
        db.session.add(new_user)
        db.session.commit()
        return {'message' : 'User registered successfully'}, 201