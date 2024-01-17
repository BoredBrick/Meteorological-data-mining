import math

from coordinates.coordinates import get_val_of_location_by_index
from data import fetch_data as fetcher
from data.process_layers import layers, get_layer_region, get_val_of_layer_by_index, get_layer_image, get_key_of_layer_by_index
from database import compress_and_upload_image as compression
from database.db_operations import insert_weather_data

location_type_area = "area"
location_type_city = "city"


def fetch_and_process_data(option, selected_layer, selected_location, selected_city):
    data_response = None
    image_response = None

    match option:
        case 1:
            data_response = get_layer_region(get_val_of_location_by_index(int(selected_location)),
                                             get_val_of_layer_by_index(int(selected_layer)))
        case 2 | 3 | 4:
            data_response = fetcher.fetch_data(selected_city)

    if option in {2, 4}:
        coords = fetcher.get_latitude_longitude(data_response)
        image_response = get_layer_region((math.floor(coords[0]) - 1, math.floor(coords[1]) - 1.5,
                                           math.ceil(coords[0]) + 1, math.ceil(coords[1]) + 1.5),
                                          get_val_of_layer_by_index(int(selected_layer)))

    process_response(option, selected_layer, selected_location, selected_city, data_response, image_response)


def process_response(option, selected_layer, selected_location, selected_city, data_response, image_response):
    match option:
        case 1 | 2:
            image_path = get_layer_image(get_key_of_layer_by_index(int(selected_layer)), image_response)
            compression.compress_and_upload_image(image_path, selected_layer,
                                                  selected_location if option == 1 else selected_city,
                                                  location_type_area if option == 1 else location_type_city)
        case 3:
            data = fetcher.data_to_json(data_response)
            insert_weather_data(data)
        case 4:
            data = fetcher.data_to_json(data_response)
            insert_id = insert_weather_data(data)

            image_path = get_layer_image(get_key_of_layer_by_index(int(selected_layer)), image_response)
            compression.compress_and_upload_image(image_path, selected_layer, selected_city, location_type_city,
                                                  insert_id)
