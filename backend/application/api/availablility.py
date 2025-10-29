from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt
from flask import request
from datetime import datetime, timedelta, date
from application.models import db, DoctorAvailability, Appointment

#  Doctor adds availability
class DoctorAvailabilityAPI(Resource):
    @jwt_required()
    def post(self):
        current_user = get_jwt()
        if current_user.get('role') != 'doctor':
            return {'message': 'Only doctors can add availability'}, 403

        data = request.get_json()
        try:
            avail_date = datetime.strptime(data.get('date'), "%Y-%m-%d").date()
            start_time = datetime.strptime(data.get('start_time'), "%H:%M").time()
            end_time = datetime.strptime(data.get('end_time'), "%H:%M").time()
        except:
            return {'message': 'Invalid date or time format'}, 400

        # allow only next 7 days
        today = date.today()
        if not (today <= avail_date <= today + timedelta(days=7)):
            return {'message': 'Availability must be within next 7 days'}, 400

        new_slot = DoctorAvailability(
            doctor_id=int(current_user.get('sub')),
            date=avail_date,
            start_time=start_time,
            end_time=end_time
        )
        db.session.add(new_slot)
        db.session.commit()
        return {'message': 'Availability added successfully'}, 201

    # Get doctor availability (patients or doctors can view)
    @jwt_required()
    def get(self):
        current_user = get_jwt()
        role = current_user.get('role')
        doctor_id = request.args.get('doctor_id', type=int)
        date_str = request.args.get('date')

        query = DoctorAvailability.query
        if doctor_id:
            query = query.filter_by(doctor_id=doctor_id)
        if date_str:
            try:
                query = query.filter_by(date=datetime.strptime(date_str, "%Y-%m-%d").date())
            except:
                return {'message': 'Invalid date format'}, 400

        availabilities = query.filter_by(status='available').all()
        return [a.convert_to_json() for a in availabilities], 200
