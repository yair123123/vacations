

from graphene import ObjectType, Int, String, List




class StudentType(ObjectType):
    id = Int()
    name = String()
    age = Int()
    favorite_language = String()
    favorite_framework = String()
    vacations = List("app.gql.types.student_vacation_types.StudentVacationType")

    def resolve_vacations(self, info):
        return self.vacations