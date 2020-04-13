from flask import Blueprint, jsonify, request
from datetime import datetime
from flask_cors import CORS

from models.attendance.AttendanceStatus import AttendanceStatus
from models.attendance.Attendance import Attendance
from models.StudentSubject import StudentSubject
from helps.Date import Date
from models import Student
from config import db

attendance = Blueprint("attendance", __name__)
CORS(attendance)

@attendance.route("<int:subject_id>/<date>", methods=["GET"])
def index(subject_id: int, date: str):
    try:
        if subject_id <= 0 or not Date.create_date(date):
            return jsonify({"error": "subject or date invalid"}), 406

        students_subjects = map(
            lambda student_subject: __local_format(student_subject),
            db.session.query(Attendance, StudentSubject).outerjoin(Attendance, 
                db.and_(Attendance.date == date, StudentSubject.id == Attendance.student_subject_id)
            ).filter( StudentSubject.subject_id == subject_id ).all()
        )

        return jsonify(list(students_subjects)), 200
    except Exception:
        return jsonify({"msg": "internal error"}), 500, 

@attendance.route("<int:subject_id>/<date>", methods=["POST","PUT"])
def register(subject_id: int, date: str):
    try:
        data = request.get_json()
        date = Date.create_date(date)

        if not subject_id or not date or not data.get("student"):
            return jsonify(
                {"error": "student, subject, date and attendance is required"}
            ), 406

        student_subject = StudentSubject.query.filter_by(
            subject_id = subject_id, student_id = data.get("student")
        ).first()

        if student_subject == None:
            return jsonify({"error": "student, subject invalid"}), 406

        status = 'PRESENTE' if data.get("attendance") else 'AUSENTE'
        status = AttendanceStatus.ATTENDANCE_STATUS[status] 

        attendance = Attendance(
            date, AttendanceStatus.query.get(status),
            student_subject
        )

        if attendance.register() == True:
            return jsonify({"msg": "success"}), 201

        return jsonify({"msg": "error"}), 500
    except Exception:
        return jsonify({"msg": "invalid request body"}), 406, 

def __local_format(student_subject) -> dict:
    if student_subject[0] is not None:
        return student_subject[0].format()
    else:
        return {**student_subject[1].format(), "attendance": None}