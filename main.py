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
            print("\u001b[36;1m---------------------------------------------------------")
            print("  A script for mining meteorological data from websites")
            print("---------------------------------------------------------\u001b[0m")
            print()
            print("\u001b[36m[1]\u001b[37m Fetch Airmass Data\u001b[0m")
            print("\u001b[36m[2]\u001b[37m Fetch Other Data\u001b[0m")
            print("\u001b[36m[0]\u001b[37m Quit Application\u001b[0m")
            option = input("\u001b[35mChoose an option:\u001b[0m ")
            print()

            match option:
                case "1":
                    print_locations()
                    location = input("\u001b[35mChoose index of location:\u001b[0m ")
                    print()
                    response = airmass.get_airmass_region(get_val_by_index(int(location)))
                    image_path = airmass.get_airmass_image(response)
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
            print()
            print("\u001b[36m---------------------------------------------------------")
            print("  A script for mining meteorological data from websites")
            print("---------------------------------------------------------\u001b[0m")
            print()
            print("\u001b[36m[1]\u001b[37m Fetch For Location\u001b[0m")
            print("\u001b[36m[2]\u001b[37m Fetch For City\u001b[0m")
            print("\u001b[36m[0]\u001b[37m Quit application\u001b[0m")
            option_location = input("\u001b[35mChoose an option:\u001b[0m ")
            print()

            match option_location:
                case "1":
                    print_locations()
                    location = input("\u001b[35mChoose an area:\u001b[0m ")
                    print()
                case "2":
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
