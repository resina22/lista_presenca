from flask import Flask
from config import app, db
from datetime import datetime
from flask_testing import TestCase

from helps.Date import Date

class Testdata(TestCase):
    def create_app(self):
        return app

    def test_create_date(self):
        assert type(Date.create_date("2020-04-02")) is datetime

    def test_date_str(self):
        assert True == (Date.text_date(datetime(2020, 4, 11)) == "2020-04-11")