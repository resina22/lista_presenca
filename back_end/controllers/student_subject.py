from flask import Blueprint, jsonify, request
from datetime import datetime
from flask_cors import CORS

from models.attendance.AttendanceStatus import AttendanceStatus
from models.attendance.Attendance import Attendance
from models.StudentSubject import StudentSubject
from models.Subject import Subject
from models.Student import Student
from helps.Date import Date
from config import db

student_subject = Blueprint("student_subject", __name__)
CORS(student_subject)

@student_subject.route("<int:subject_id>", methods=["GET"])
def index(subject_id: int):
    try:
        students_subjects = map(
            lambda student_subject: student_subject.format(),
            StudentSubject.query.filter_by(subject_id = subject_id).all()
        )

        return jsonify(list(students_subjects)), 200
    except Exception:
        return jsonify({"msg": "internal error"}), 500, 


@student_subject.route("<int:subject_id>", methods=["POST"])
def associate(subject_id: int):
    try:
        data = request.get_json()
        if not data.get("student") or not subject_id:
            return jsonify({"error": "student and subject is required"}), 406

        student = Student.query.get(data.get("student"))
        subject = Student.query.get(subject_id)

        if student == None or subject == None:
            return jsonify({"error": "student or subject is required"}), 406

        result = (StudentSubject(student, subject)).save()

        if result == True:
            return jsonify({"msg": "success"}), 201

        return jsonify({"msg": "error"}), 500
    except Exception:
        return jsonify({"msg": "invalid request body"}), 406, 
