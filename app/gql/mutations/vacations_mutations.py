from graphene import Mutation, InputObjectType, Date, Int, Field

from app.db.models import StudentVacation
from app.db.repository.student_vacation_repository import insert_vacation
from app.db.services.validation_service import insert_vacation_with_validation
from app.gql.query import Query
from app.gql.types.student_vacation_types import StudentVacationType


class VacationInput(InputObjectType):
    start_vacation = Date()
    end_vacation = Date()
    student_id = Int()
    country_id = Int()


class CreateVacation(Mutation):
    class Arguments:
        vacationInput = VacationInput()

    vacation = Field(StudentVacationType)

    @staticmethod
    def mutate(root, info, vacationInput):
        return CreateVacation(vacation=Query.check_response(insert_vacation(StudentVacation(**vacationInput))))


class CreateVacationWithValidation(Mutation):
    class Arguments:
        vacationInput = VacationInput()

    vacation = Field(StudentVacationType)
    @staticmethod
    def mutate(root, info, vacationInput):
        return CreateVacation(vacation=Query.check_response(insert_vacation_with_validation(StudentVacation(**vacationInput))))

