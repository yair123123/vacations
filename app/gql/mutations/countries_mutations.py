from graphene import Mutation, InputObjectType, String, Field

from app.db.models import Country
from app.db.repository.country_repository import insert_country
from app.gql.query import Query
from app.gql.types.country_type import CountryType


class CountryInput(InputObjectType):
    name = String()
    region = String()
    capital = String()


class CreateCountry(Mutation):
    class Arguments:
        countryInput = CountryInput()

    country = Field(CountryType)

    @staticmethod
    def mutate(root, info, countryInput):
        return CreateCountry(country=Query.check_response(insert_country(Country(**countryInput))))
