import argparse
import math
import sys
import time
import warnings

import keyboard
from PIL import Image

from coordinates.coordinates import get_val_of_location_by_index
from coordinates.coordinates import print_locations
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
            print("\n \u001b[36;1m---------------------------------------------------------")
            print("  A script for mining meteorological data from websites")
            print("---------------------------------------------------------\u001b[0m \n")
            print("\u001b[36m[1]\u001b[37m Fetch Meteorological Satellite Images\u001b[0m")
            print("\u001b[36m[2]\u001b[37m Fetch Meteorological Data\u001b[0m")
            print("\u001b[36m[0]\u001b[37m Quit Application\u001b[0m")
            option = input("\u001b[35mChoose an option:\u001b[0m ")
            print()

            match option:
                case "1":
                    layers.print_layers()
                    layer = input("\u001b[35mChoose index of layer:\u001b[0m ")
                    print()
                    print_locations()
                    location = input("\u001b[35mChoose index of location:\u001b[0m ")
                    print()

                    response = layers.get_layer_region(get_val_of_location_by_index(int(location)),
                                                       layers.get_val_of_layer_by_index(int(layer)))
                    image_path = layers.get_layer_image(layers.get_key_of_layer_by_index(int(layer)), response)
                    image = Image.open(image_path)  # import to database
                    image.show()

                case "2":
                    city = input("\u001b[35mChoose a city:\u001b[0m ")
                    print()
                    response = fetcher.fetch_data(city)
                    fetcher.get_data(response)
                    data = fetcher.data_to_json(response)  # import to database

                case "0":
                    break

                case _:
                    continue

        elif args["fetch"] == "all":
            print("\n \u001b[36m---------------------------------------------------------")
            print("  A script for mining meteorological data from websites")
            print("---------------------------------------------------------\u001b[0m \n")
            print("\u001b[36m[1]\u001b[37m Fetch Data For Location\u001b[0m")
            print("\u001b[36m[2]\u001b[37m Fetch Data For City\u001b[0m")
            print("\u001b[36m[0]\u001b[37m Quit application\u001b[0m")
            option_location = input("\u001b[35mChoose an option:\u001b[0m ")
            print()

            layer = ""
            location = ""
            city = ""
            match option_location:
                case "1":
                    layers.print_layers()
                    layer = input("\u001b[35mChoose index of layer:\u001b[0m ")
                    print()
                    print_locations()
                    location = input("\u001b[35mChoose index of location:\u001b[0m ")
                    print()
                case "2":
                    layers.print_layers()
                    layer = input("\u001b[35mChoose index of layer:\u001b[0m ")
                    print()
                    city = input("\u001b[35mChoose a city:\u001b[0m ")
                    print()
                case "0":
                    break
                case _:
                    continue

            print("\u001b[36m[1]\u001b[37m Fetch once\u001b[0m")
            print("\u001b[36m[2]\u001b[37m Endless fetching\u001b[0m")
            option_fetching = input("\u001b[35mChoose an option:\u001b[0m ")
            print()

            while not keyboard.is_pressed('q'):
                if option_location == "1":
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

                if option_fetching == "1":
                    break
                else:
                    try:
                        time.sleep(layer_update_time)
                    except KeyboardInterrupt:
                        break


if __name__ == "__main__":
    main()
