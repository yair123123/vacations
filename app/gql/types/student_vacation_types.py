from graphene import ObjectType, Int, Date, Field

from app.db.models import Student, Country
from app.gql.types.country_type import CountryType
from app.gql.types.student_types import StudentType


class StudentVacationType(ObjectType):
    id = Int()
    start_vacation = Date()
    end_vacation = Date()
    student_id = Int()
    country_id = Int()
    student = Field(lambda :StudentType)
    country = Field(lambda :CountryType)