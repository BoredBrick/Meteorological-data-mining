import datetime as dt

import requests

import authentification.credentials as credentials

# OPEN WEATHER MAP API guide - https://openweathermap.org/current

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"


def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9 / 5) + 32
    return celsius, fahrenheit


def fetch_data(city=None) -> requests.models.Response:
    # fetch data
    url = BASE_URL + "appid=" + credentials.api_key + "&q=" + city
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


def get_latitude_longitude(response=None):
    return response['coord']['lat'], response['coord']['lon']
