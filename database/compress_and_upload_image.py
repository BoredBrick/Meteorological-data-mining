from coordinates.coordinates import get_key_of_location_by_index
from data.process_layers import get_key_of_layer_by_index
from database import db_operations
from image_manipulation import compression


def compress_and_upload_image(image_path, layer, location):
    layer = get_key_of_layer_by_index(int(layer))
    location = get_key_of_location_by_index(int(location))
    compression.compress_until_smaller_than_one_mb(image_path, image_path)
    db_operations.insert_image_into_database(image_path, layer, location)
