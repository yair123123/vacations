from app.settings.config import session_maker
from app.db.models import Student
from app.utils.csv_util import read_csv


def insert_all_csv_to_db():
    path = "data.csv"
    students = []
    for row in read_csv(path):
        row = {k.lower():v for k ,v in row.items()}
        student = Student(**row)
        students.append(student)
    with session_maker() as session:
        session.add_all(students)
        session.commit()
