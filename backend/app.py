from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from datetime import timedelta, datetime
import os

from application.models import db, User
from application.api.auth import LoginApi, RegisterApi
from application.api.doctor import DoctorApi, DoctorDetailApi, DoctorProfileUpdateAPI
from application.api.patient import PatientApi, PatientProfileUpdateAPI
from application.api.department import DepartmentApi
from application.api.appointment import AppointmentApi, AppointmentPaymentAPI
from application.api.treatment import (
    TreatmentAdd, DoctorPatientHistory,
    PatientTreatmentHistory, AdminTreatmentHistory,
    ExportDataAPI
)
from application.api.availablility import (
    DoctorAvailabilityAPI, DoctorAvailabilityWeekAPI
)
from application.api.chart import AppointmentReportApi, DepartmentDemandApi
from application.api.pdf import PDFReportAPI
from application.api1 import WelcomeApi, cache

from flask_cors import CORS
from application.worker import celery


# ------------------------------------------------------------------
# APP SETUP
# ------------------------------------------------------------------

base_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
CORS(app, supports_credentials=True)

# ------------------------------------------------------------------
# DATABASE CONFIG
# ------------------------------------------------------------------

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(base_dir, "database.sqlite3")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# ------------------------------------------------------------------
# SECURITY
# ------------------------------------------------------------------

app.config["SECRET_KEY"] = "hospital-apps-secret"
app.config["JWT_SECRET_KEY"] = "hospital-secret"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=12)

# ------------------------------------------------------------------
# REDIS (OPTIONAL – RENDER)
# ------------------------------------------------------------------

REDIS_URL = os.environ.get("REDIS_URL")

if REDIS_URL:
    app.config['CACHE_TYPE'] = 'RedisCache'
    app.config['CACHE_REDIS_URL'] = REDIS_URL

    celery.conf.update(
        broker_url=REDIS_URL,
        result_backend=REDIS_URL,
        timezone='Asia/Kolkata'
    )
else:
    # fallback (local / no redis)
    app.config['CACHE_TYPE'] = 'SimpleCache'

app.config['CACHE_DEFAULT_TIMEOUT'] = 300

# ------------------------------------------------------------------
# INIT EXTENSIONS
# ------------------------------------------------------------------

db.init_app(app)
cache.init_app(app)

api = Api(app)
jwt = JWTManager(app)

# ------------------------------------------------------------------
# API ROUTES
# ------------------------------------------------------------------

api.add_resource(WelcomeApi, '/api/welcome')

api.add_resource(LoginApi,
                 '/api/login',
                 '/api/account/<string:account_type>/<int:account_id>')

api.add_resource(RegisterApi, '/api/register')

api.add_resource(DoctorApi,
                 '/api/doctor',
                 '/api/doctor/<int:doctor_id>')

api.add_resource(DoctorProfileUpdateAPI,
                 '/api/doctor/me',
                 '/api/doctor/profile-update')

api.add_resource(DoctorDetailApi,
                 '/api/doctor-details/<int:doctor_id>')

api.add_resource(PatientApi,
                 '/api/patient',
                 '/api/patient/<int:patient_id>')

api.add_resource(PatientProfileUpdateAPI,
                 '/api/patient/profile-update')

api.add_resource(DepartmentApi,
                 '/api/department',
                 '/api/department/<int:department_id>')

api.add_resource(AppointmentApi,
                 '/api/appointment',
                 '/api/appointment/<int:appointment_id>')

api.add_resource(AppointmentPaymentAPI,
                 '/api/appointments/<int:appointment_id>/pay')

api.add_resource(TreatmentAdd,
                 '/api/treatment/<int:appointment_id>')

api.add_resource(DoctorPatientHistory,
                 '/api/treatment/doctor')

api.add_resource(PatientTreatmentHistory,
                 '/api/treatment/patient')

api.add_resource(AdminTreatmentHistory,
                 '/api/treatment/admin')

api.add_resource(DoctorAvailabilityAPI,
                 '/api/availability')

api.add_resource(DoctorAvailabilityWeekAPI,
                 '/api/availability-week')

api.add_resource(ExportDataAPI,
                 '/api/treatment/export')

api.add_resource(AppointmentReportApi,
                 '/api/report/appointments-trend')

api.add_resource(DepartmentDemandApi,
                 '/api/report/department-demand')

api.add_resource(PDFReportAPI,
                 '/api/reports/monthly')

# ------------------------------------------------------------------
# TEST CACHE
# ------------------------------------------------------------------

@app.route('/test_cache')
@cache.cached(timeout=10)
def test_cache():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"message": f"Cache working at {now}"}

# ------------------------------------------------------------------
# DB INIT (CRITICAL FOR RENDER)
# ------------------------------------------------------------------

def add_admin():
    admin = User.query.filter_by(role='admin').first()
    if not admin:
        admin = User(
            name='Admin',
            email='admin@gmail.com',
            password='123456',
            role='admin'
        )
        db.session.add(admin)
        db.session.commit()


with app.app_context():
    db.create_all()
    add_admin()

# ------------------------------------------------------------------
# GUNICORN ENTRYPOINT
# ------------------------------------------------------------------
# DO NOT use app.run() on Render
