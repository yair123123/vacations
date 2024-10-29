from typing import List

from returns.result import Failure, Success, Result
from sqlalchemy.exc import SQLAlchemyError

from app.settings.config import session_maker
from app.db.models import Country
from app.db.models.student import Student
def insert_student(student:Student):
    try:
        with session_maker() as session:
            session.add(student)
            session.commit()
            session.refresh(student)
            return Success(student)
    except SQLAlchemyError as e:
        return Failure(str(e))
def get_all_students():
    try:
        with session_maker() as session:
            students = session.query(Student).all()
            return Success(students)
    except SQLAlchemyError as e:
        return Failure(str(e))
def get_student_by_id(student_id:int)-> Result[Student,Failure]:
    try:
        with session_maker() as session:
            student = session.get(Student,student_id)
            if student == None:
                return Failure("not found")
            return Success(student)
    except SQLAlchemyError as e:
        return Failure(str(e))
def get_students_by_country(country_name:str) -> Result[List[Student],Failure]:
    try:
        with session_maker() as session:
            students = session.query(Student).filter(Student.vacation.country.name == country_name).all()
            if students is []:
                return Failure("not found")
            return Success(students)
    except SQLAlchemyError as e:
        return Failure(str(e))

