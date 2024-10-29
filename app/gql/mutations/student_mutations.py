from graphene import Field, InputObjectType, String, Int, Mutation

from app.db.models import Student
from app.db.repository.student_repository import insert_student
from app.gql.query import Query
from app.gql.types.student_types import StudentType


class StudentInput(InputObjectType):
    name = String()
    age = Int()
    favorite_language = String()
    favorite_framework = String()


class CreateStudent(Mutation):
    class Arguments:
        studentInput = StudentInput()

    student = Field(StudentType)

    @staticmethod
    def mutate(root, info, studentInput):
        return CreateStudent(student=Query.check_response(insert_student(Student(**studentInput))))
