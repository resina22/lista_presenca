
from flask import jsonify

from config import app, db
from controllers.student import student
from controllers.subject import subject
from controllers.attendance import attendance
from controllers.student_subject import student_subject

db.create_all()

@app.errorhandler(404)
def page_not_found(e):
    return jsonify("Página não encontrada"), 404

app.register_blueprint(student, url_prefix="/students")
app.register_blueprint(subject, url_prefix="/subjects")
app.register_blueprint(student_subject, url_prefix="/students_subjects")
app.register_blueprint(attendance, url_prefix="/attendances")

if __name__ == '__main__':
    app.run(
        host = app.config['HOST'],
        port = app.config['PORT'],
        debug = app.config['DEBUG']
    )