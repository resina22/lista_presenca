from flask import Flask
from datetime import datetime
from flask_testing import TestCase

from config import app, db
from models import Subject, Student
from models.StudentSubject import StudentSubject
from models.attendance.Attendance import Attendance
from models.attendance.AttendanceStatus import AttendanceStatus

class TestAttendance(TestCase):
    def create_app(self):
        return app

    def test_subject(self):
        attendance = Attendance(
            datetime.now().date(),
            AttendanceStatus.query.get(2),
            StudentSubject.query.get(1)
        )

        assert attendance.register() == True
