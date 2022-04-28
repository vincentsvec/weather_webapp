from django.http import HttpResponse
import os
import csv
import json
import difflib
from django.shortcuts import render, redirect
from .api import get_weather_data, get_location_weather_data
from .models import User_data


def index(request):
    """
    Home page.
    """
    if str(request.user) != "AnonymousUser":
        user_data = request.user.user_data.first()

    else:
        user_data = None

    location_weather_data = None

    weather_data = []

    if user_data != None and user_data.saved_cities != None:
        for city in user_data.saved_cities:
            weather_data.append([city, get_weather_data(request, city, True)])

    location = request.body.decode('utf-8')
    if 'location' in location:
        location = json.loads(location)
        lat = location.get('location')[0]
        lon = location.get('location')[1]

        user_data.location = [lat, lon]
        user_data.save()

    if user_data != None and user_data.location != None:
        location_weather_data = get_location_weather_data(
            request, user_data.location[0], user_data.location[1])

    else:
        location_weather_data = None

    return render(request, 'main/index.html', {'weather_data': weather_data, "location_weather_data": location_weather_data})


def city_results(request):
    """
    City results after searching for city. Renders page with list of avaiable cities.
    """
    # loads cities from cities database
    local_dir = os.path.dirname(__file__)
    file_path = os.path.join(local_dir, "../cities_database/worldcities.csv")
    cities_file = open(file_path)
    scvreader = csv.reader(cities_file)

    cities = []

    if request.method == 'POST':
        searched_city = request.POST.get('city')

        for row in scvreader:
            if row[0].startswith(searched_city.title()):
                cities.append(row[0] + ", " + row[4] + ", " + row[7])

        cities = sorted(cities, key=lambda x: difflib.SequenceMatcher(
            None, x, searched_city.title()).ratio(), reverse=True)

    cities = cities[: 15]

    return render(request, "main/city_results.html", {"cities": cities, "searched_city": searched_city})


def city_view(request, city_name):
    """
    City weather details.
    """
    city_id = city_name

    weather_data = get_weather_data(request, city_name)

    city_details = city_name.split(", ")[1] + ", " + city_name.split(", ")[2]
    city_name = city_name.split(", ")[0]

    return render(request, "main/city_view.html", {
        "weather_data": weather_data,
        "city_id": city_id,
        "city_name": city_name,
        "city_details": city_details,
    })


def change_unit(request):
    if request.method == "POST":

        user_data = request.user.user_data.first()

        if user_data.weather_unit == "metric":
            user_data.weather_unit = "imperial"

        else:
            user_data.weather_unit = "metric"

        user_data.save()

        url = request.POST.get("back")

        if url != "":
            return redirect(url)

        else:
            return redirect("/")


def add_city(request, city_id):
    user_data = request.user.user_data.first()

    if city_id not in user_data.saved_cities:
        user_data.saved_cities.append(city_id)
        user_data.save()

    return redirect("/cities/" + city_id)


def remove_city(request, city_id):
    user_data = request.user.user_data.first()

    user_data.saved_cities.remove(city_id)
    user_data.save()

    return redirect("/")
