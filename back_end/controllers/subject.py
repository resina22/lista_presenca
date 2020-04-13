from flask import Blueprint, jsonify, request
from flask_cors import CORS

from config import db
from models.Subject import Subject

subject = Blueprint("subject", __name__)
CORS(subject)

@subject.route("", methods=["GET"])
def index():
    try:
        subjects = map(
            lambda subject: subject.format(), Subject.query.all()
        )

        return jsonify(list(subjects)), 200
    except Exception:
        return jsonify({"msg": "internal error"}), 500, 

@subject.route("", methods=["POST"])
def create():
    try:
        data = request.get_json()
        if not data.get("name"):
            return jsonify({"error": "name is required"}), 406

        result = (Subject(data.get("name"))).save()
        if result == True:
            return jsonify({"msg": "success"}), 201

        return jsonify({"msg": "error"}), 500
    except Exception:
        return jsonify({"msg": "invalid request body"}), 406,
