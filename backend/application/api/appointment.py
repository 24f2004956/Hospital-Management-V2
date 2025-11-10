from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt
from datetime import datetime, date
from ..models import db, Appointment, DoctorAvailability
from ..api1 import cache

class AppointmentApi(Resource):
    @jwt_required()
    def post(self):
        current_user = get_jwt()
        if current_user.get('role') != "patient":
            return {'message':'Only Patients can  make Appointments '}, 403
        
        data = request.get_json()
        if not (data.get('doctor_id') and data.get('date') and data.get('time')):
            return {'message' : 'Bad request! doctor_id, date, and time are required.'}, 400
        
        try:
            appt_date = datetime.strptime(data['date'], "%Y-%m-%d").date()
            appt_time = datetime.strptime(data['time'], "%H:%M").time()
        except ValueError:
            return {'message': 'Invalid date or time format. Use YYYY-MM-DD and HH:MM.'}, 400
        
        slot = DoctorAvailability.query.filter(
            DoctorAvailability.doctor_id == int(data['doctor_id']),
            DoctorAvailability.date == appt_date,
            DoctorAvailability.start_time <= appt_time,
            DoctorAvailability.end_time >= appt_time,
            DoctorAvailability.status == 'available'
        ).first()


        if not slot:
            return {'message': 'No available slot found for this doctor at that time.'}, 400


    
        existing_appointment = Appointment.query.filter_by(doctor_id=data.get('doctor_id'), date=appt_date, time=appt_time, status='Booked').first()
        if existing_appointment:
            return {'message':'This doctor already has an appointment at that date and time'}, 400  

        new_appointment=Appointment(doctor_id=data.get('doctor_id'),
            patient_id=current_user.get('sub'),
            date = appt_date,
            time = appt_time,
            status='Booked',
            reason=data.get('reason') )
        
        db.session.add(new_appointment)
        slot.status = 'booked'
        db.session.commit()
        return {
            'message': 'Appointment booked successfully.',
            'appointment': new_appointment.convert_to_json()
        }, 201
    
# rest of the appointment jobs i.e delete, update, and fetch (get to be updated accordingly for now its ai logic and ofcource it is not correct )
    @jwt_required()
    def delete(self, appointment_id):
        current_user = get_jwt()

        appointment = Appointment.query.get(appointment_id)
        if not appointment:
            return {'message': 'Appointment not found.'}, 404

        # Only the patient who booked it or an admin can cancel
        print(get_jwt())
        if current_user.get('role') not in ['admin', 'patient'] or (
            current_user.get('role') == 'patient' and appointment.patient_id != int(current_user.get('sub'))):
            return {'message': 'You are not authorized to cancel this appointment.'}, 403

        if appointment.status == 'Cancelled':
            return {'message': 'Appointment already cancelled.'}, 400

        appointment.status = 'Cancelled'

        # Update the slot back to 'available'
        slot = DoctorAvailability.query.filter_by(
            doctor_id=appointment.doctor_id,
            date=appointment.date,
            start_time=appointment.time
        ).first()
        if slot:
            slot.status = 'available'
        db.session.commit()

        return {'message': 'Appointment cancelled successfully.'}, 200

       
    @jwt_required()
    def put(self, appointment_id):
        current_user = get_jwt()
        appointment = Appointment.query.get(appointment_id)

        if not appointment:
            return {'message': 'Appointment not found.'}, 404

        # Only doctor of that appointment or admin can update
        if current_user.get('role') == 'doctor' and appointment.doctor_id != int(current_user.get('sub')):
            return {'message': 'You are not authorized to update this appointment.'}, 403

        data = request.get_json()
        updated_status = data.get('status')

        if updated_status not in ['Booked', 'Completed', 'Cancelled']:
            return {'message': 'Invalid status value.'}, 400

        appointment.status = updated_status
        appointment.reason = data.get('reason', appointment.reason)

        # Sync slot status with appointment status
        slot = DoctorAvailability.query.filter_by(
            doctor_id=appointment.doctor_id,
            date=appointment.date,
            start_time=appointment.time
        ).first()
        if slot:
            if updated_status == 'Cancelled':
                slot.status = 'available'
            elif updated_status == 'Booked':
                slot.status = 'booked'

        db.session.commit()

        return {
            'message': f'Appointment status updated to {updated_status}.',
            'appointment': appointment.convert_to_json()
        }, 200
    
    @jwt_required()
    #@cache.cached(timeout=60)
    def get(self):
        current_user = get_jwt()
        role = current_user.get('role')

        if role == 'patient':
            appointments = Appointment.query.filter(Appointment.patient_id == int(current_user.get('sub')),Appointment.date >= date.today(),Appointment.status == 'Booked').all()
        elif role == 'doctor':
            appointments = Appointment.query.filter(Appointment.doctor_id == int(current_user.get('sub')),Appointment.date >= date.today(),Appointment.status == 'Booked').all()
        else:  # admin
            appointments = Appointment.query.filter(Appointment.date >= date.today(), Appointment.status == 'Booked'  ).all()
        appointment_json = []
        for appointment in appointments:
            appointment_json.append(appointment.convert_to_json())
        return appointment_json, 200 

   


