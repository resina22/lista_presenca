from config import db
from models.attendance import Attendance

class AttendanceStatus(db.Model):
    __tablename__ = "attendance_status"

    id = db.Column( db.Integer, primary_key=True, autoincrement=True)
    status = db.Column(db.String(45), nullable=False, unique=True)

    attendance = db.relationship("Attendance", backref=db.backref("attendances.status_id"))
    ATTENDANCE_STATUS = {'PRESENTE': 1, 'AUSENTE': 2}

    def __init__(self, status: str):
        self.status = status

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
            "status": self.status,
        }