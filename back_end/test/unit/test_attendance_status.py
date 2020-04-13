from flask import Flask
from datetime import datetime
from flask_testing import TestCase

from config import app, db
from models.attendance.AttendanceStatus import AttendanceStatus

class TestAttendanceStatus(TestCase):
    def create_app(self):
        return app

    def test_create_subject(self):
        result_status = [
            (AttendanceStatus('Presente')).save(),
            (AttendanceStatus('Ausente')).save()
        ]
        # assert not False in result_status

        # attendance_status = AttendanceStatus('Presente')
        # assert attendance_status.save() == False

        # attendance_status = AttendanceStatus('Ausente')
        # assert attendance_status.save() == False

    def test_filter(self):
        pass
        