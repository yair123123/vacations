from typing import List

from returns.result import Failure, Success, Result
from sqlalchemy.exc import SQLAlchemyError

from app.db.models import StudentVacation, Student, Country
from app.settings.config import session_maker


def insert_vacation(vacation: StudentVacation):
    try:
        with session_maker() as session:
            session.add(vacation)
            session.commit()
            session.refresh(vacation)
            return Success(vacation)
    except SQLAlchemyError as e:
        return Failure(str(e))


def get_student_vacation_by_id(student_vacation_id: int) -> StudentVacation:
    try:
        with session_maker() as session:
            student_vacation_id = session.get(StudentVacation, student_vacation_id)
            if student_vacation_id is None:
                return Failure("not found")
            return Success(student_vacation_id)
    except SQLAlchemyError as e:
        return Failure(str(e))


def get_all_vacations_by_student_id(student_id: int) -> Result[List[StudentVacation], Failure]:
    try:
        with session_maker() as session:
            vacation_by_student = session.query(StudentVacation).filter(StudentVacation.student_id == student_id).all()
            if vacation_by_student is []:
                return Failure("not found")
            return Success(vacation_by_student)
    except SQLAlchemyError as e:
        return Failure(str(e))


def get_students_and_region(region: str) -> Result[List[Student], Failure]:
    try:
        with session_maker() as session:
            countries_id_in_region = session.query(Country).with_entities(Country.id).filter(
                Country.region == region).all()
            students = (
                session.query(Student)
                .filter(Student.vacations.any(StudentVacation.country_id.in_(countries_id_in_region)))
                .all()
            )
            if students == []:
                return Failure("not found")
            return Success(students)
    except SQLAlchemyError as e:
        return Failure(str(e))


def get_vacations_by_date(start_date, end_date):
    try:
        with session_maker() as session:
            vacations = session.query(StudentVacation).filter(
                (StudentVacation.start_vacation > start_date) & (StudentVacation.end_vacation < end_date)).all()
            if vacations == []:
                return Failure("not found")
            return Success(vacations)
    except SQLAlchemyError as e:
        return Failure(str(e))


def get_vacations_longer_by_days(days):
    try:
        with session_maker() as session:
            vacations = session.query(StudentVacation).all()
            vacations_longer_by_days = []
            for x in vacations:
                start = x.start_vacation.split("-")[2]
                end = x.end_vacation.split("-")[2]
                duration = end - start
                if duration >= days:
                    vacations_longer_by_days.append(x)
            if vacations_longer_by_days == []:
                return Failure("not found")
    except SQLAlchemyError as e:
        return Failure(str(e))
