from datetime import datetime
from io import BytesIO

import mysql.connector as mysql
from PIL import Image

from authentication import credentials


def connect_to_database():
    db_connection = mysql.connect(host=credentials.server_host_ip, database=credentials.database_name,
                                  user=credentials.database_user, password=credentials.database_password)

    print("Connected to:", db_connection.get_server_info())

    return db_connection


def insert_image_into_database(image_path, layer, location):
    db_connection = connect_to_database()

    cursor = db_connection.cursor()

    try:
        with open(image_path, 'rb') as image_file:

            sql_insert_query = "INSERT INTO radar_images (date, layer, location, image) VALUES (%s, %s, %s, %s)"

            date = datetime.now()
            layer = layer
            location = location
            image_data = image_file.read()

            data = (date, layer, location, image_data)

            cursor.execute(sql_insert_query, data)

            db_connection.commit()

            print("The image has been successfully inserted into database")

    except mysql.Error as error:
        print(f"Error inserting the image into the database: {error}")

    finally:
        cursor.close()
        db_connection.close()


def retrieve_image_from_database(image_id):
    db_connection = connect_to_database()

    cursor = db_connection.cursor()

    try:
        sql_select_query = "SELECT image FROM radar_images WHERE id = %s"
        data = (image_id,)

        cursor.execute(sql_select_query, data)

        result = cursor.fetchone()

        if result is not None:
            image_data = result[0]

            image = Image.open(BytesIO(image_data))

            image.show()

        else:
            print("The image with the given ID was not found")

    except mysql.Error as error:
        print(f"Error loading image from database: {error}")

    finally:
        cursor.close()
        db_connection.close()
