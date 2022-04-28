"""
Weather api requests
"""
import os
import csv
import requests
from .models import User_data


def get_weather_data(request, city_name, simplify=False):
    """
    Fetch data from openweather api. Takes city name and if simplify mode is True. Returns complete or basic weather_data.
    """
    # loads cities from cities database
    local_dir = os.path.dirname(__file__)
    file_path = os.path.join(local_dir, "../cities_database/worldcities.csv")
    cities_file = open(file_path)
    scvreader = csv.reader(cities_file)

    for row in scvreader:
        if row[0] + ", " + row[4] + ", " + row[7] == city_name:
            lon, lat = row[3], row[2]

    if str(request.user) != "AnonymousUser":
        user_data = request.user.user_data.first()
        unit = user_data.weather_unit

    else:
        unit = "metric"

    API_KEY = os.environ.get('API_KEY')

    if simplify:
        url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units={unit}&appid={API_KEY}'
    else:
        url = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units={unit}&exclude=minutely&appid={API_KEY}'

    weather_data = requests.get(url).json()

    return weather_data


def get_location_weather_data(request, lat, lon):
    user_data = request.user.user_data.first()
    unit = user_data.weather_unit

    API_KEY = os.environ.get('API_KEY')
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units={unit}&appid={API_KEY}'

    weather_data = requests.get(url).json()

    return weather_data
