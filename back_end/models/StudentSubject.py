from config import app, db
from helps.Date import Date
from models import Subject, Student
from models.attendance import Attendance

class StudentSubject(db.Model):
    __tablename__ = "students_subjects"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    subject_id = db.Column(
        db.Integer, db.ForeignKey("subjects.id"), nullable=False
    )
    student_id = db.Column(
        db.Integer, db.ForeignKey("students.id"), nullable=False
    )

    student = db.relationship(
        "Student", backref=db.backref("students")
    )

    subject = db.relationship(
        "Subject", backref=db.backref("subjects")
    )

    attendance = db.relationship(
        "Attendance", backref=db.backref("attendances")
    )

    __table_args__ = (
        db.UniqueConstraint(
            'subject_id', 'student_id', name='unique_subject_student'
        ),
    )

    def __init__(self, student: Student, subject: Subject):
        self.student_id = student.id
        self.subject_id = subject.id

    def save(self) -> bool:
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except Exception:
            db.session.rollback()
            return False

    def format(self) -> dict:
        return {
            "id": self.id,
            "student": {
                "id": self.student.id,
                "name": self.student.name
            },
            "subject": {
                "id": self.subject.id,
                "name": self.subject.name
            }
        }