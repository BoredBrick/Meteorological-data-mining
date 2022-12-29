import datetime as dt
import json

import requests
import unidecode as unidecode

import authentication.credentials as credentials

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


# this method is used only for tests
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

    print(response)


def get_data(response=None) -> dict:
    time_of_data_calc = dt.datetime.utcfromtimestamp(response['dt'] + response['timezone'])  # time of data calculation
    city = response['name']  # city name
    latitude = response['coord']['lat']  # city geo location, latitude
    longitude = response['coord']['lon']  # city geo location, longitude

    weather = response['weather'][0]['main']  # group of weather parameters (Rain, Snow, Extreme etc.)
    description = response['weather'][0]['description']  # weather condition within the group

    temp_kelvin = response['main']['temp']  # temperature [kelvin]
    temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)  # temperature [celsius, fahrenheit]
    feels_like_kelvin = response['main']['feels_like']  # temperature, human perception of weather [kelvin]
    feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(
        feels_like_kelvin)  # temperature, human perception of weather [celsius, fahrenheit]
    pressure = response['main']['pressure']  # atmospheric pressure [hPa]
    humidity = response['main']['humidity']  # humidity [%]
    temp_min_kelvin = response['main']['temp_min']  # minimum temperature at the moment [kelvin]
    temp_min_celsius, temp_min_fahrenheit = kelvin_to_celsius_fahrenheit(
        temp_min_kelvin)  # minimum temperature at the moment [celsius, fahrenheit]
    temp_max_kelvin = response['main']['temp_max']  # maximum temperature at the moment [kelvin]
    temp_max_celsius, temp_max_fahrenheit = kelvin_to_celsius_fahrenheit(
        temp_max_kelvin)  # maximum temperature at the moment [celsius, fahrenheit]

    visibility = response['visibility']  # visibility [meter]

    wind_speed = response['wind']['speed']  # wind speed [meter/sec]
    wind_deg = response['wind']['deg']  # wind direction [degrees]

    clouds = response['clouds']['all']  # cloudiness [%]

    sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])  # sunrise time
    sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])  # sunset time

    data = {
        "time_of_data_calc": time_of_data_calc,
        "city": unidecode(city),
        "latitude": latitude,
        "longitude": longitude,
        "weather": weather,
        "description": description,
        "temp_kelvin": temp_kelvin,
        "temp_celsius": round(temp_celsius, 2),
        "temp_fahrenheit": round(temp_fahrenheit, 2),
        "feels_like_kelvin": feels_like_kelvin,
        "feels_like_celsius": round(feels_like_celsius, 2),
        "feels_like_fahrenheit": round(feels_like_fahrenheit, 2),
        "temp_min_kelvin": temp_min_kelvin,
        "temp_min_celsius": round(temp_min_celsius, 2),
        "temp_min_fahrenheit": round(temp_min_fahrenheit, 2),
        "temp_max_kelvin": temp_max_kelvin,
        "temp_max_celsius": round(temp_max_celsius, 2),
        "temp_max_fahrenheit": round(temp_max_fahrenheit, 2),
        "pressure": pressure,
        "humidity": humidity,
        "visibility": visibility,
        "wind_speed": wind_speed,
        "wind_deg": wind_deg,
        "clouds": clouds,
        "sunrise_time": sunrise_time,
        "sunset_time": sunset_time
    }

    return data


def data_to_json(response=None) -> str:
    json_object = json.dumps(get_data(response), default=str, indent=4)
    print(json_object)
    return json_object


def get_latitude_longitude(response=None) -> tuple:
    return response['coord']['lat'], response['coord']['lon']
