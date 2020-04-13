from datetime import datetime

from config import db
from helps.Date import Date
from models.attendance import AttendanceStatus
from models import Subject, Student, StudentSubject

class Attendance(db.Model):
    __tablename__ = "attendances"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Date, nullable=False)

    status_id = db.Column(
        db.Integer, db.ForeignKey("attendance_status.id"), nullable=False
    )

    student_subject_id = db.Column(
        db.Integer, db.ForeignKey("students_subjects.id"), nullable=False
    )

    student_subject = db.relationship(
        "StudentSubject", backref=db.backref("students_subjects")
    )

    status = db.relationship(
        "AttendanceStatus", backref=db.backref("attendance_status")
    )

    __table_args__ = (
        db.UniqueConstraint(
            'student_subject_id', 'date', name='unique_subject_student_date'
        ),
    )

    def __init__(
        self, date: datetime.date, status: AttendanceStatus,
        student_subject: StudentSubject
    ):
        self.date = date
        self.status_id = status.id
        self.student_subject_id = student_subject.id

    def register(self) -> bool:
        try:
            registered = Attendance.query.filter_by(
                date = Date.text_date(self.date), student_subject_id = self.student_subject_id
            ).first()

            if registered is not None:
                registered.status_id = self.status_id
                db.session.commit()
            else:
                db.session.add(self)
                db.session.commit()

            return True
        except Exception as e:
            print(e)
            db.session.rollback()
            return False

    def format(self):
        return {
            "student": {
                "id": self.student_subject.student.id,
                "name": self.student_subject.student.name
            },
            "subject": {
                "id": self.student_subject.subject.id,
                "name": self.student_subject.subject.name
            },
            "attendance": {
                "id": self.id,
                "status_id": self.status.id,
                "status": self.status.status
            }
        }