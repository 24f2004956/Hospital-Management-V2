from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token,jwt_required, get_jwt_identity
from .models import db,User

#api testing
# 200- ok, 201-created new record, 404-notfound, 400-bad req., 401-auth, 403-auth, 405
class WelcomeApi(Resource):
    @jwt_required()
    def get(self):
        return {'message':'hello, this is hospital management app'},200
    
    def post(self):
        data = request.get_json() # request.json  also works
        print(request)
        print(data)
        msg = f'hello{data.get("name")}'
        return {'message':msg},200
    
class LoginApi(Resource):
    def post(self):
        data=request.get_json()

        if not (data.get('email') and data.get('password')):
            return {'message' : 'Both email & password fields are required.'}, 400
        
        user=User.query.filter_by(email=data.get('email')).first()

        if not user:
            return {'message' : 'User not found.'}, 404
        
        if user.password != data.get('password'):
            return {'message' : 'Incorrect password'}, 400
        
        token = create_access_token({'role' : user.role, 'user_id' : user.id})
        '''token = create_access_token(
                                    identity=str(user.id),              # string for JWT "sub"
                                    additional_claims={"role": user.role}  # extra info
                                )'''
        
        return {
                'message': 'User logged in successfully.',
                'token' : token,
                'user_name' : user.name,
                'user_role' : user.role
                }, 200
        
        

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
        
        new_user=User(name=data.get('name').strip(), email=data.get('email').strip(), password=data.get('password').strip())
        db.session.add(new_user)
        db.session.commit()
        return {'message' : 'User registered successfully'}, 201
          