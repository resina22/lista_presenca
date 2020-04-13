from flask import Flask
from flask_testing import TestCase
from config import app, db

from models.Subject import Subject

class TestSubject(TestCase):
    def create_app(self):
        return app

    def test_create_subject(self):
        subject = Subject("Física")
        assert subject.save() == True

        subject = Subject("Física")
        assert subject.save() == False

    def test_filter(self):
        subject = Subject.query.filter_by(name = "Física").all()
        assert subject is not None