from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt
from ..models import db, Treatment, Appointment, User, Doctor
from ..task import data_export

class TreatmentAdd(Resource):
    @jwt_required()
    def post(self, appointment_id):
        current_user = get_jwt()
        role = current_user.get('role')

        # Only doctors can add treatment
        if role != 'doctor':
            return {'message': 'Only doctors can add or update treatments'}, 403

        appointment = Appointment.query.filter_by(id=appointment_id).first()
        if not appointment:
            return {'message': 'Appointment not found'}, 404

        # Optional: Verify that this doctor owns the appointment
        if appointment.doctor_id != int(current_user.get('sub')):
            return {'message': 'You are not authorized to update this appointment'}, 403

        data = request.get_json()

        # Check if treatment already exists for this appointment
        treatment = Treatment.query.filter_by(appointment_id=appointment_id).first()
        if not treatment:
            treatment = Treatment(appointment_id=appointment_id)

        treatment.diagnosis = data.get('diagnosis')
        treatment.prescription = data.get('prescription')
        treatment.notes = data.get('notes')
        treatment.visit_type = data.get('visit_type')
        treatment.test_done = data.get('test_done')
        treatment.medicines = data.get('medicines')

        db.session.add(treatment)
        db.session.commit()

        return {'message': 'Treatment record saved successfully'}, 200
    

class DoctorPatientHistory(Resource):
    @jwt_required()
    def get(self):
        current_user = get_jwt()
        if current_user.get('role') != 'doctor':
            return {'message': 'Access denied!'}, 403

        doctor_id = int(current_user.get('sub'))

        # Get all appointments for this doctor
        appointments = Appointment.query.filter_by(doctor_id=doctor_id).all()
        appointment_ids = [appt.id for appt in appointments]

        treatments = Treatment.query.filter(Treatment.appointment_id.in_(appointment_ids)).all()
        return [t.convert_to_json() for t in treatments], 200

class PatientTreatmentHistory(Resource):
    @jwt_required()
    def get(self):
        current_user = get_jwt()
        if current_user.get('role') != 'patient':
            return {'message': 'Access denied!'}, 403

        patient_id = int(current_user.get('sub'))

        # Get all appointments for this patient
        appointments = Appointment.query.filter_by(patient_id=patient_id).all()
        appointment_ids = [appt.id for appt in appointments]

        treatments = Treatment.query.filter(Treatment.appointment_id.in_(appointment_ids)).all()
        return [t.convert_to_json() for t in treatments], 200


class AdminTreatmentHistory(Resource):
    @jwt_required()
    def get(self):
        current_user = get_jwt()
        if current_user.get('role') != 'admin':
            return {'message': 'Admin access only!'}, 403

        treatments = Treatment.query.all()
        return [t.convert_to_json() for t in treatments], 200


class ExportDataAPI(Resource):
    @jwt_required()
    def get(self):
        current_user = get_jwt()
        if current_user.get('role') != 'patient':
            return {'message': 'Access denied!'}, 403

        patient_id = int(current_user.get('sub'))

        # Get all appointments for this patient
        appointments = Appointment.query.filter_by(patient_id=patient_id).all()
        appointment_ids = [appt.id for appt in appointments]


       
        #treatments = Treatment.query.filter(Treatment.appointment_id.in_(appointment_ids)).all()
        treatments = (
            db.session.query(Treatment, Appointment, Doctor)
            .join(Appointment, Treatment.appointment_id == Appointment.id)
            .join(Doctor, Appointment.doctor_id == Doctor.id)  # doctor
            .filter(Treatment.appointment_id.in_(appointment_ids))
            .all()
        )
        patient = User.query.get(patient_id)

        treatment_details = []
        for treatment, appointment, doctor in treatments:
            treatment_details.append({"name": patient.name,
                                      "doctor_name":doctor.name,
                                        "diagnosis": treatment.diagnosis,
                                        "prescription": treatment.prescription,
                                        "notes": treatment.notes,
                                        "upcoming_visit":appointment.date,
                                        "visit_type": treatment.visit_type,
                                        "test_done": treatment.test_done,
                                        "medicines": treatment.medicines })
            
        data_export(treatment_details, patient.email)
        return {"message": "Your data export task has been initiated, Please check your inbox"}, 200 