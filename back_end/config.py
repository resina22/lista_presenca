import os
import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['HOST'] = '127.0.0.1'
app.config['PORT'] = 8080
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/attendance_list.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'sqlite:///db/attendance_list.sqlite3'

db = SQLAlchemy(app)