from flask import Blueprint, jsonify, request
from flask_cors import CORS

from models.Student import Student
from config import app, db

student = Blueprint("student", __name__)
CORS(student)

@student.route("", methods=["GET"])
def index():
    try:
        students = map(
            lambda student: student.format(), Student.query.all()
        )

        return jsonify(list(students)), 200
    except Exception:
        return jsonify({"msg": "internal error"}), 500, 

@student.route("", methods=["POST"])
def create():
    try:
        data = request.get_json()
        if not data.get("name"):
            return jsonify({"error": "name is required"}), 406

        result = (Student(data.get("name"))).save()
        if result == True:
            return jsonify({"msg": "success"}), 201

        return jsonify({"msg": "error"}), 500
    except Exception:
        return jsonify({"msg": "invalid request body"}), 406, 
