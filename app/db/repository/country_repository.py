from typing import List

from flask import session
from returns.result import Failure, Success, Result
from sqlalchemy.exc import SQLAlchemyError


from app.db.models import Country
from app.settings.config import session_maker

def insert_country(country:Country):
    try:
        with session_maker() as session:
            session.add(country)
            session.commit()
            session.refresh(country)
            return Success(country)
    except SQLAlchemyError as e:
        return Failure(str(e))

def get_country_by_id(country_id:int)-> Result[Country,Failure]:
    try:
        with session_maker() as session:
            country = session.get(Country, country_id)
            if country is None:
                return Failure("not found")
            return Success(country)
    except SQLAlchemyError as e:
        return Failure(str(e))
def add_all_countries(countries:List[Country]) -> Result:
    try:
        with session_maker() as session:
            session.add_all(countries)
            session.commit()
            return Success("countries is added successfully")
    except SQLAlchemyError as e:
        return Failure(str(e))