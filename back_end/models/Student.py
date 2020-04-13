from config import app, db
from models import Subject, StudentSubject

class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    subjects = db.relationship("Subject", secondary="students_subjects")

    def __init__(self, name: str):
        self.name = name

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
            "name": self.name,
        }