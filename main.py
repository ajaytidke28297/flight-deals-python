import requests
from pprint import  pprint
from flight_search import FlightSearch
from dotenv import load_dotenv
import os

load_dotenv()

SHEETY_ENDPOINT = "https://api.sheety.co/90203dcb0b578ada8862d86b9cefcc1e/flightDeals/prices"
response = requests.get(url=SHEETY_ENDPOINT)
response.raise_for_status()
sheet_data = response.json()['prices']
flight_search = FlightSearch()

for city in sheet_data:
    iata = flight_search.get_iata_code(city['city'])
    city['city'] = iata
    city_body = {
        "price": {
            "iataCode": iata,
        }
    }
    response_put = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}", json=city_body)
    response_put.raise_for_status()
