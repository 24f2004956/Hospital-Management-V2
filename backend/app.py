from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from application.models import db, User
from application.api import WelcomeApi, LoginApi, RegisterApi
from datetime import timedelta

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
app.config["SECRET_KEY"] = "hospital-apps-secret" # protects sessions, cookies, and tokens from being tampered with.
app.config["JWT_SECRET_KEY"] = "hospital-secret" # protects jwt key for authentication
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=12) 

db.init_app(app)
api = Api(app)
jwt= JWTManager(app)
app.app_context().push()

api.add_resource(WelcomeApi, '/api/welcome')
api.add_resource(LoginApi, '/api/login')
api.add_resource(RegisterApi, '/api/register')

def add_admin():
    admin = User.query.filter_by(role = 'admin').first()
    if not admin:
        admin = User(name = 'Admin', email = 'admin@gmail.com', password = '123456', role='admin')
        db.session.add(admin)
        db.session.commit()
        print('admin created in database successfully')
    else:
        print('admin already exist in database')
        
if __name__=='__main__':
    add_admin()
    db.create_all()
    app.run(debug=True)