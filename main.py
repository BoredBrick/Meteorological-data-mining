import argparse
import sys
import time
import warnings
import math
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
            print()
            print("[1] Fetch For Location")
            print("[2] Fetch For City")
            print("[0] Quit application")
            option_location = input("Choose an option: ")

            match option_location:
                case "1":
                    print_locations()
                    location = input("Choose an area: ")

                case "2":
                    city = input("Choose a city: ")

                case "0":
                    break

                case _:
                    continue

            print()
            print("[1] Fetch once")
            print("[2] Endless fetching")
            option_fetching = input("Choose an option: ")

            while not keyboard.is_pressed('q'):

                if option_location == "1":
                    response = airmass.get_airmass_region(get_val_by_index(int(location)))
                    image_path = airmass.get_airmass_image(response)
                    image = Image.open(image_path)  # import to database
                    #image.show()
                else:
                    response = fetcher.fetch_data(city)
                    fetcher.get_data(response)
                    data = fetcher.data_to_json(response)  # import to database
                    coords = fetcher.get_latitude_longitude(response)

                    response = airmass.get_airmass_region((math.floor(coords[0]) - 1, math.floor(coords[1]) - 1,
                                                           math.ceil(coords[0]) + 1, math.ceil(coords[1]) + 1))
                    image_path = airmass.get_airmass_image(response)
                    image = Image.open(image_path)  # import to database
                    # image.show()

                if option_fetching == "1":
                    break
                else:
                    waiting = 0
                    while not keyboard.is_pressed('q'):
                        waiting += 0.1
                        if waiting >= 10:
                            break
                        time.sleep(0.1)

if __name__ == "__main__":
    main()
