from typing import List

from returns.result import Failure

from app.db.models import StudentVacation
from app.db.repository.student_vacation_repository import get_all_vacations_by_student_id, insert_vacation


def insert_vacation_with_validation(vacation:StudentVacation):
    vacations_by_student_id= get_all_vacations_by_student_id(vacation.student_id)
    if vacations_by_student_id.unwrap() == []:
        return insert_vacation(vacation)
    for vacation_already_exist  in vacations_by_student_id.unwrap():
        if (vacation.start_vacation >= vacation_already_exist.start_vacation and vacation.start_vacation <= vacation_already_exist.end_vacation) or (vacation.end_vacation <= vacation_already_exist.end_vacation and vacation.end_vacation >= vacation_already_exist.start_vacation):
            return Failure("vacation_already_exist")
        return insert_vacation(vacation)