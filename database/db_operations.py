import json
from datetime import datetime
from io import BytesIO

import mysql.connector as mysql
from PIL import Image

from authentication import credentials


def connect_to_database():
    db_connection = mysql.connect(host=credentials.server_host_ip, database=credentials.database_name,
                                  user=credentials.database_user, password=credentials.database_password)
    return db_connection


def insert_image_into_database(image_path, layer, location, weather_data_id):
    db_connection = connect_to_database()
    cursor = db_connection.cursor()

    try:
        sql_insert_query = "INSERT INTO radar_images (date, weather_data_id, layer, location, image) VALUES (%s, " \
                            "%s, %s, %s, %s)"

        date = datetime.now()
        weather_data_id = weather_data_id
        layer = layer
        location = location
        image_data = image_path

        data = (date, weather_data_id, layer, location, image_data)

        cursor.execute(sql_insert_query, data)

        db_connection.commit()

    except mysql.Error as error:
        print(f"Error inserting the image into the database: {error}")

    finally:
        cursor.close()
        db_connection.close()


def insert_weather_data(json_data):
    db_connection = connect_to_database()
    cursor = db_connection.cursor()

    try:
        data = json.loads(json_data)
        cursor = db_connection.cursor()

        sql = '''INSERT INTO weather_info (
                    time_of_data_calc, city, latitude, longitude, weather, description,
                    temp_kelvin, temp_celsius, temp_fahrenheit, feels_like_kelvin,
                    feels_like_celsius, feels_like_fahrenheit, temp_min_kelvin,
                    temp_min_celsius, temp_min_fahrenheit, temp_max_kelvin,
                    temp_max_celsius, temp_max_fahrenheit, pressure, humidity,
                    visibility, wind_speed, wind_deg, clouds, sunrise_time, sunset_time
                )
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''

        values = (
            data['time_of_data_calc'], data['city'], data['latitude'], data['longitude'],
            data['weather'], data['description'], data['temp_kelvin'], data['temp_celsius'],
            data['temp_fahrenheit'], data['feels_like_kelvin'], data['feels_like_celsius'],
            data['feels_like_fahrenheit'], data['temp_min_kelvin'], data['temp_min_celsius'],
            data['temp_min_fahrenheit'], data['temp_max_kelvin'], data['temp_max_celsius'],
            data['temp_max_fahrenheit'], data['pressure'], data['humidity'], data['visibility'],
            data['wind_speed'], data['wind_deg'], data['clouds'], data['sunrise_time'],
            data['sunset_time']
        )

        cursor.execute(sql, values)
        print("The weather data has been successfully inserted into database")


    except mysql.Error as error:
        print(f"Error inserting weather data into the database: {error}")

    finally:
        cursor.close()
        db_connection.close()
        return cursor.lastrowid


def retrieve_image_from_database(date):
    db_connection = connect_to_database()

    cursor = db_connection.cursor()

    try:
        sql_select_query = "SELECT image FROM radar_images WHERE date = %s"
        data = (date,)

        cursor.execute(sql_select_query, data)

        result = cursor.fetchone()

        if result is not None:
            image_path = result[0]

            image = Image.open(image_path)

            image.show()

        else:
            print("The image with the given ID was not found")

    except mysql.Error as error:
        print(f"Error loading image from database: {error}")

    finally:
        cursor.close()
        db_connection.close()
