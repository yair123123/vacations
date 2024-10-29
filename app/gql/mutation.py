from graphene import ObjectType

from app.gql.mutations.countries_mutations import CreateCountry
from app.gql.mutations.student_mutations import CreateStudent
from app.gql.mutations.vacations_mutations import CreateVacation, CreateVacationWithValidation


class Mutations(ObjectType):
    createCountry = CreateCountry.Field()
    createStudent = CreateStudent.Field()
    createVacation = CreateVacation.Field()
    createVacationWithValidation = CreateVacationWithValidation().Field()
    # deleteJob = DeleteJob.Field()
    # updateEmployee = UpdateEmployee.Field()
    # updateJob = UpdateJob.Field()
