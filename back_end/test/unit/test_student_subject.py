from flask import Flask
from flask_testing import TestCase

from config import app, db
from models.StudentSubject import StudentSubject
from models.Subject import Subject
from models.Student import Student

class TestStudentSubject(TestCase):
    def create_app(self):
        return app

    def test_create_subject(self):
        student = Student.query.filter_by(name = "Pedro").first()
        subject = Subject.query.filter_by(name = "Física").first()
        student_subject = StudentSubject(student, subject)

        assert student_subject.save() == True

        student_subject = StudentSubject(student, subject)
        assert student_subject.save() == False

    def test_filter(self):
        subject = Subject.query.filter_by(name = "Física").first()
        student_subject = StudentSubject.query.filter_by(subject_id = subject.id )
        assert student_subject is not None