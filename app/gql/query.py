from graphene import ObjectType, Field, List, Int, String, Date
from graphql import GraphQLError
from returns.result import Success, Result

from app.db.models import StudentVacation, Student
from app.db.repository.country_repository import get_country_by_id
from app.db.repository.student_repository import get_student_by_id, get_students_by_country, get_all_students
from app.db.repository.student_vacation_repository import get_student_vacation_by_id, get_all_vacations_by_student_id, \
    get_students_and_region, get_vacations_by_date, get_vacations_longer_by_days
from app.gql.types.country_type import CountryType
from app.gql.types.student_types import StudentType
from app.gql.types.student_vacation_types import StudentVacationType


class Query(ObjectType):
    @staticmethod
    def check_response(response):
        result:Result = response
        if isinstance(result,Success):
            return result.unwrap()
        else:
            raise GraphQLError(str(result))
    all_students = List(StudentType)
    student_by_id = Field(StudentType,studentId=Int())
    country_by_id = Field(CountryType,countryId=Int())
    vacation_by_id = Field(StudentVacationType,vacationId=Int())
    students_by_country = List(StudentType,countryName=String())
    vacations_by_student_id = List(StudentVacationType,studentId=Int())
    student_by_region = List(StudentType,region=String())
    get_vacations_by_date = List(StudentVacationType,StartDate=Date(),EndDate=Date())
    get_vacations_longer_by_days=List(StudentVacationType,days=Int())

    @staticmethod
    def resolve_all_students(root,info):
        return Query.check_response(get_all_students())
    @staticmethod
    def resolve_student_by_id(root, info, studentId):
        return Query.check_response(get_student_by_id(studentId))
    @staticmethod
    def resolve_country_by_id(root,info,countryId):
        return Query.check_response(get_country_by_id(countryId))
    @staticmethod
    def resolve_vacation_by_id(root,info,vacationId):
        return Query.check_response(get_student_vacation_by_id(vacationId))

    @staticmethod
    def resolve_students_by_country(root,info,countryName):
        return Query.check_response(get_students_by_country(countryName))

    @staticmethod
    def resolve_vacations_by_student_id(root,info,studentId):
        return Query.check_response(get_all_vacations_by_student_id(studentId))

    @staticmethod
    def resolve_student_by_region(root,info,region):
        return Query.check_response(get_students_and_region(region))

    @staticmethod
    def resolve_get_vacations_by_date(root,info,StartDate,EndDate):
        return Query.check_response(get_vacations_by_date(StartDate,EndDate))
    @staticmethod
    def resolve_get_vacations_longer_by_days(root,info,days):
        return Query.check_response(get_vacations_longer_by_days(days))

