from app.api.countries_api import get_all_countries_from_api
from app.db.models import Country


def create_objects_countries():
    countries = get_all_countries_from_api()
    objects_country = [Country(
        name=country.get("name", {}).get("common", None) if country.get("name") else None,
        region=country.get("region", None),
        capital=country.get("capital", [])[0] if country.get("capital") else None
    ) for country in countries if country]
    return objects_country

