from flask import Flask
from flask_testing import TestCase
from config import app, db

from models.Student import Student

class TestStudent(TestCase):
    def create_app(self):
        return app

    def test_create_student(self):
        student = Student("Pedro")
        assert student.save() == True

        student = Student("Pedro")
        assert student.save() == False

    def test_filter(self):
        student = Student.query.filter_by(name = "Pedro").all()
        assert student is not None