import datetime as dt

import requests

# OPEN WEATHER MAP API guide - https://openweathermap.org/current

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
# API_KEY = open('api_key', 'r').read()
API_KEY = "1e71cfe93daced52e4c97934b1f9576b"


# CITY = "Split"

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9 / 5) + 32
    return celsius, fahrenheit


def fetch_data(city=None) -> requests.models.Response:
    # fetch data
    url = BASE_URL + "appid=" + API_KEY + "&q=" + city
    response = requests.get(url).json()
    return response


def print_data(response=None):
    city = response['name']
    temp_kelvin = response['main']['temp']
    temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
    feels_like_kelvin = response['main']['feels_like']
    feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)
    wind_speed = response['wind']['speed']
    humidity = response['main']['humidity']
    description = response['weather'][0]['description']
    sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
    sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

    # print data
    print(f"Temperature in {city}: {temp_celsius:.2f}°C or {temp_fahrenheit:.2f}°F")
    print(f"Temperature in {city} feels like: {feels_like_celsius:.2f}°C or {feels_like_fahrenheit:.2f}°F")
    print(f"Humidity in {city}: {humidity}%")
    print(f"Wind Speed in {city}: {wind_speed}m/s")
    print(f"General Weather in {city}: {description}")
    print(f"Sun rises in {city}: {sunrise_time} local time")
    print(f"Sun sets in {city}: {sunset_time} local time")

    # print(response)
