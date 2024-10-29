
from graphene import ObjectType, Int, String, List


class CountryType(ObjectType):
    id = Int()
    name = String()
    region = String()
    capital = String()
    vacations = List("app.gql.types.student_vacation_types.StudentVacationType")

    def resolve_vacations(self, info):
        return self.vacations