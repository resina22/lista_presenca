from datetime import datetime

class Date(object):
    def __init__(self):
        pass

    @staticmethod
    def create_date(date: str) -> datetime.date or bool:
        try:
            return datetime.strptime(date, "%Y-%m-%d")
        except Exception:
            return False

    @staticmethod
    def text_date(date: datetime.date) -> str:
        try:
            return datetime.strftime(date, "%Y-%m-%d")
        except Exception:
            return False
