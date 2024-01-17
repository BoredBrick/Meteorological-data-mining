import os

from coordinates.coordinates import get_key_of_location_by_index
from data.process_layers import get_key_of_layer_by_index
from database import db_operations
from image_manipulation import compression


def compress_and_upload_image(image_path, layer, location, location_type, weather_data_id=None):
    layer = get_key_of_layer_by_index(int(layer))
    if weather_data_id is None and location_type == "area":
        location = get_key_of_location_by_index(int(location))
    compression.compress_until_smaller_than_one_mb(image_path, image_path)
    db_operations.insert_image_into_database(image_path, layer, location, weather_data_id, location_type)
#    os.remove(image_path)
