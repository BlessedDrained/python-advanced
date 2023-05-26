import csv
from flask import Flask, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from task_1 import Student

app = Flask(__name__)
engine = create_engine('sqlite:///sqlite_python.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

UPLOAD_FOLDER = 'static/files'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if __name__ == '__main__':
    app.run(port=5001)


@app.route('/students/upload', methods=['POST'])
def upload_students():
    file = request.files['file']
    students = []
    for row in csv.DictReader(file, delimiter=';'):
        student_data = {
            'name': row['name'],
            'surname': row['surname'],
            'phone': row['phone'],
            'email': row['email'],
            'average_score': float(row['average_score']),
            'scholarship': row['scholarship']
        }
        students.append(student_data)

    try:
        session.bulk_insert_mappings(Student, students)
        session.commit()
        return 'Student list has been loaded'
    except:
        return "An error occured", 500
