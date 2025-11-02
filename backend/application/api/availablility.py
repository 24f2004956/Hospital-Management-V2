from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt
from flask import request
from datetime import datetime, timedelta, date
from application.models import db, DoctorAvailability, Appointment

SLOTS = {
    1: ("07:30", "09:30"),
    2: ("10:00", "12:00"),
    3: ("14:30", "16:30"),
    4: ("17:00", "19:00"),
    5: ("20:30", "21:30")
}

class DoctorAvailabilityAPI(Resource):
    @jwt_required()
    def post(self):
        current_user = get_jwt()
        if current_user.get('role') != 'doctor':
            return {'message': 'Only doctors can add availability'}, 403

        data = request.get_json()
        slot_id = data.get('slot_id')
        date_str = data.get('date')

        if slot_id not in SLOTS:
            return {'message': 'Invalid slot ID'}, 400

        start_str, end_str = SLOTS[slot_id]
        avail_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        start_time = datetime.strptime(start_str, "%H:%M").time()
        end_time = datetime.strptime(end_str, "%H:%M").time()

        today = date.today()
        if not (today <= avail_date <= today + timedelta(days=7)):
            return {'message': 'Date must be within next 7 days'}, 400

        # Prevent Duplicate Slot
        existing = DoctorAvailability.query.filter_by(
            doctor_id=current_user.get('sub'),
            date=avail_date,
            start_time=start_time,
            end_time=end_time
        ).first()

        if existing:
            return {'message': 'Slot already exists'}, 400

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
    
class DoctorAvailabilityWeekAPI(Resource):
    @jwt_required()
    def get(self):
        current_user = get_jwt()
        if current_user.get('role') != 'doctor':
            return {'message': 'Only doctors can view their availability'}, 403

        doctor_id = int(current_user.get('sub'))
        today = date.today()
        next_week = today + timedelta(days=7)

        slots = DoctorAvailability.query.filter(
            DoctorAvailability.doctor_id == doctor_id,
            DoctorAvailability.date >= today,
            DoctorAvailability.date <= next_week
        ).all()

        return [s.convert_to_json() for s in slots], 200
    
    @jwt_required()
    def post(self):
        current_user = get_jwt()
        if current_user.get('role') != 'doctor':
            return {'message': 'Only doctors can add availability'}, 403

        data = request.get_json()
        date_str = data.get('date')
        slot_id = data.get('slot_id')

        if slot_id not in SLOTS:
            return {'message': 'Invalid slot ID'}, 400

        start_str, end_str = SLOTS[slot_id]
        avail_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        start_time = datetime.strptime(start_str, "%H:%M").time()
        end_time = datetime.strptime(end_str, "%H:%M").time()

        # Prevent duplicate slot
        exists = DoctorAvailability.query.filter_by(
            doctor_id=int(current_user.get('sub')),
            date=avail_date,
            start_time=start_time,
            end_time=end_time
        ).first()

        if exists:
            db.session.delete(exists)   # ✅ Toggle behavior (remove if exists)
            db.session.commit()
            return {'message': 'Slot removed'}, 200

        # Otherwise add slot
        new_slot = DoctorAvailability(
            doctor_id=int(current_user.get('sub')),
            date=avail_date,
            start_time=start_time,
            end_time=end_time
        )
        db.session.add(new_slot)
        db.session.commit()
        return {'message': 'Slot added'}, 201

