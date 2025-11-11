from ..models import db
from flask_restful import Resource

from flask_jwt_extended import jwt_required, get_jwt
from sqlalchemy import text

class AppointmentReportApi(Resource):
    @jwt_required()
    def get(self):
        current_user = get_jwt()
        if current_user.get("role") != "admin":
            return {"message": "Access denied"}, 403

        query = text("""
            SELECT
                date AS date,
                COUNT(id) AS count
            FROM appointment
            WHERE appointment.status != 'Cancelled'        
            GROUP BY date
            ORDER BY date ASC
        """)

        result = db.session.execute(query)

        data = [{"date": str(row.date), "count": row.count} for row in result]

        return data, 200
    
class DepartmentDemandApi(Resource):
    @jwt_required()
    def get(self):
        current_user = get_jwt()
        if current_user.get("role") != "admin":
            return {"message": "Access denied"}, 403


        query = text("""
            SELECT 
                d.name AS department,
                COUNT(a.id) AS count
            FROM appointment a
            JOIN doctor doc ON a.doctor_id = doc.id
            JOIN department d ON doc.department_id = d.id
            WHERE a.status != 'Cancelled'
            GROUP BY d.name
            ORDER BY count DESC
        """)

        result = db.session.execute(query)


        data = [{"department": row.department, "count": row.count} for row in result]

        return data, 200

 
