from config import app, db
from models import Student

class Subject(db.Model):
    __tablename__ = "subjects"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False, unique=True)
    students = db.relationship("Student", secondary="students_subjects")

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
            "name": self.name
        }