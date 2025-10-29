from flask import request, current_app as app
from flask_restful import Resource
from flask_jwt_extended import create_access_token,jwt_required, get_jwt_identity,get_jwt
from .models import db,User,Doctor
from flask_caching import Cache
import time

cache = Cache()

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
    

          

