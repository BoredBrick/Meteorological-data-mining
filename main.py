import argparse
import math
import sys
import time
import warnings

import keyboard
from PIL import Image

from coordinates.coordinates import get_val_by_index
from coordinates.coordinates import print_locations
from data import fetch_data as fetcher
from data import process_airmass as airmass

warnings.simplefilter("ignore")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--fetch", required=False, help="all - start fetching all possible data")
    args = vars(ap.parse_args())

    while True:

        if len(sys.argv) < 2:
            print()
            print("[1] Fetch Airmass Data")
            print("[2] Fetch Other Data")
            print("[0] Quit application")
            option = input("Choose an option: ")

            match option:
                case "1":
                    print_locations()
                    location = input("Choose a location: ")
                    response = airmass.get_airmass_region(get_val_by_index(int(location)))
                    image_path = airmass.get_airmass_image(response)
                    image = Image.open(image_path)  # import to database
                    image.show()

                case "2":
                    city = input("Choose a city: ")
                    response = fetcher.fetch_data(city)
                    fetcher.get_data(response)
                    data = fetcher.data_to_json(response)  # import to database

                case "0":
                    break

                case _:
                    continue

        elif args["fetch"] == "all":
            city = input("Choose a city: ")

            print("[1] Fetch once")
            print("[2] Endless fetching")
            option = input("Choose an option: ")

            while not keyboard.is_pressed('q'):
                response = fetcher.fetch_data(city)
                fetcher.get_data(response)
                data = fetcher.data_to_json(response)  # import to database
                coords = fetcher.get_latitude_longitude(response)

                response = airmass.get_airmass_region((math.floor(coords[0]) - 1, math.floor(coords[1]) - 1,
                                                       math.ceil(coords[0]) + 1, math.ceil(coords[1]) + 1))
                image_path = airmass.get_airmass_image(response)
                image = Image.open(image_path)  # import to database
                # image.show()

                if option == "1":
                    break
                else:
                    waiting = 0
                    while not keyboard.is_pressed('q'):
                        waiting += 0.1
                        if waiting >= 10:
                            break
                        time.sleep(0.1)
                        print(waiting)


if __name__ == "__main__":
    main()
