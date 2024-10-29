import requests

URL = "https://restcountries.com/v3.1/all"
def get_all_countries_from_api():
    response = requests.get(URL)
    return response.json()
