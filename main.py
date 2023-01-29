import argparse
import math
import sys
import warnings

from PIL import Image

from console_prints import *
from coordinates.coordinates import get_val_of_location_by_index
from data import fetch_data as fetcher
from data import process_layers as layers

warnings.simplefilter("ignore")

layer_update_time = 10 * 60


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--fetch", required=False, help="all - start fetching all possible data")
    args = vars(ap.parse_args())

    while True:
        if len(sys.argv) < 2:
            option = select_fetching()
            match option:
                case "1":
                    layer = select_layer()
                    location = select_location()
                    response = layers.get_layer_region(get_val_of_location_by_index(int(location)),
                                                       layers.get_val_of_layer_by_index(int(layer)))
                    image_path = layers.get_layer_image(layers.get_key_of_layer_by_index(int(layer)), response)
                    image = Image.open(image_path)  # import to database
                    image.show()

                case "2":
                    city = select_city()
                    response = fetcher.fetch_data(city)
                    fetcher.get_data(response)
                    data = fetcher.data_to_json(response)  # import to database

                case "0":
                    break

                case _:
                    continue

        elif args["fetch"] == "all":
            option = select_all_fetching()
            layer = select_layer()
            location = ""
            city = ""
            match option:
                case "1":
                    location = select_location()
                case "2":
                    city = select_city()
                case "0":
                    break
                case _:
                    continue

            endless_fetching = select_endless_fetching()
            while True:
                if option == "1":
                    response = layers.get_layer_region(get_val_of_location_by_index(int(location)),
                                                       layers.get_val_of_layer_by_index(int(layer)))
                    image_path = layers.get_layer_image(layers.get_key_of_layer_by_index(int(layer)), response)
                    image = Image.open(image_path)  # import to database
                    # image.show()
                else:
                    response = fetcher.fetch_data(city)
                    fetcher.get_data(response)
                    data = fetcher.data_to_json(response)  # import to database
                    coords = fetcher.get_latitude_longitude(response)

                    response = layers.get_layer_region((math.floor(coords[0]) - 1, math.floor(coords[1]) - 1.5,
                                                        math.ceil(coords[0]) + 1, math.ceil(coords[1]) + 1.5),
                                                       layers.get_val_of_layer_by_index(int(layer)))
                    image_path = layers.get_layer_image(layers.get_key_of_layer_by_index(int(layer)), response)
                    image = Image.open(image_path)  # import to database
                    # image.show()

                if endless_fetching == "1":
                    break
                else:
                    try:
                        time.sleep(layer_update_time)
                    except KeyboardInterrupt:
                        break


if __name__ == "__main__":
    main()
