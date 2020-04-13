INSERT OR IGNORE INTO attendance_status(status) VALUES ('Presente'), ('Ausente');
INSERT OR IGNORE INTO subjects(name) VALUES ('Física'), ('Inglês'), ('Química'), ('Artes'), ('Biologia'), ('Espanhol'), ('Geografia'), ('História'), ('Português'), ('Redação');
INSERT OR IGNORE INTO students(name) VALUES ('João Miguel'), ('Enzo Gabriel'), ('Maria Cecilia'), ('Maria Eduarda'), ('Maria Alice'), ('João Lucas'), ('Ana Julia'), ('Maria Clara'), ('João Pedro');
INSERT OR IGNORE INTO students_subjects(student_id, subject_id ) SELECT id, 1 FROM students;
