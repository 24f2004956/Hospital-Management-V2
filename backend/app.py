from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from application.models import db, User
from application.api.auth import LoginApi, RegisterApi
from application.api.doctor import DoctorApi, DoctorDetailApi, DoctorProfileUpdateAPI
from application.api.patient import PatientApi, PatientProfileUpdateAPI
from application.api.department import DepartmentApi
from application.api.appointment import AppointmentApi, AppointmentPaymentAPI
from application.api.treatment import TreatmentAdd, DoctorPatientHistory, PatientTreatmentHistory, AdminTreatmentHistory, ExportDataAPI
from application.api.availablility import  DoctorAvailabilityAPI, DoctorAvailabilityWeekAPI
from application.worker import celery
from application.api.chart import AppointmentReportApi, DepartmentDemandApi
from application.api.pdf import PDFReportAPI
from application.task import *
#from flask_cors import CORS

from application.api1 import WelcomeApi, cache
from datetime import timedelta, datetime
import os

base_dir = os.path.abspath(os.path.dirname(__file__))


app=Flask(__name__)
#CORS(app, supports_credentials=True)
#CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(base_dir, "database.sqlite3")
app.config["SECRET_KEY"] = "hospital-apps-secret" # protects sessions, cookies, and tokens from being tampered with.
app.config["JWT_SECRET_KEY"] = "hospital-secret" # protects jwt key for authentication
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=12) 

app.config['CACHE_TYPE'] = 'redis'
app.config['CACHE_REDIS_HOST'] = 'localhost'  # Or your Redis host
app.config['CACHE_REDIS_PORT'] = 6379         # Or your Redis port
app.config['CACHE_REDIS_DB'] = 0              # Or your Redis database index
app.config['CACHE_REDIS_URL'] = "redis://localhost:6379"         
app.config['CACHE_DEFAULT_TIMEOUT'] = 300    

celery.conf.update(
    broker_url = 'redis://localhost:6379/0',
    result_backend = 'redis://localhost:6379/1',
    timezone = 'Asia/Kolkata' )



db.init_app(app)
cache.init_app(app)
#celery.init_app(app)
api = Api(app)
jwt= JWTManager(app)
app.app_context().push()

api.add_resource(WelcomeApi, '/api/welcome')
api.add_resource(LoginApi, '/api/login', '/api/account/<string:account_type>/<int:account_id>')
api.add_resource(RegisterApi, '/api/register')
api.add_resource(DoctorApi, '/api/doctor', '/api/doctor/<int:doctor_id>')
api.add_resource(DoctorProfileUpdateAPI, '/api/doctor/me',  '/api/doctor/profile-update')
api.add_resource(DoctorDetailApi,   '/api/doctor-details/<int:doctor_id>')
api.add_resource(PatientApi, '/api/patient', '/api/patient/<int:patient_id>')
api.add_resource(PatientProfileUpdateAPI, '/api/patient/profile-update' ,)
api.add_resource(DepartmentApi, '/api/department', '/api/department/<int:department_id>')
api.add_resource(AppointmentApi, '/api/appointment', '/api/appointment/<int:appointment_id>')
api.add_resource(TreatmentAdd, '/api/treatment/<int:appointment_id>',)
api.add_resource(DoctorPatientHistory, '/api/treatment/doctor',)
api.add_resource(PatientTreatmentHistory, '/api/treatment/patient',)
api.add_resource(AdminTreatmentHistory, '/api/treatment/admin',)
api.add_resource(DoctorAvailabilityAPI, '/api/availability',)
api.add_resource(DoctorAvailabilityWeekAPI, '/api/availability-week')
api.add_resource(ExportDataAPI, '/api/treatment/export',)
api.add_resource(AppointmentReportApi, '/api/report/appointments-trend',)
api.add_resource(DepartmentDemandApi, '/api/report/department-demand',)
api.add_resource(PDFReportAPI, '/api/reports/monthly')
api.add_resource(AppointmentPaymentAPI, '/api/appointments/<int:appointment_id>/pay')



@app.route('/test_cache')
@cache.cached(timeout=10)
def test_cache():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"Test is working. Current time: {now}"

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
    #db.drop_all() #toggle b/w drop_all() and add admin
    add_admin()
    db.create_all()
    app.run(debug=True)