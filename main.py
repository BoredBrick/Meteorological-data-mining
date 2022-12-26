import argparse
import math
import os
import sys
import time
import urllib.request
import warnings

from coordinates.coordinates import Coordinates
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
                    response = airmass.get_airmass_region(Coordinates.WESTERN_EUROPE)

                    folder_name = "AIRMASS//"  # Donwload the files in a folder with the name of the product
                    os.makedirs(folder_name, exist_ok=True)
                    img_landing = folder_name + time.strftime("%Y_%m_%d-%H_%M_%S") + ".jpg"
                    urllib.request.urlretrieve(response.url, img_landing)
                    print("Image of Airmass was stored successfully!")

                case "2":
                    city = input("Choose a city: ")
                    response = fetcher.fetch_data(city)
                    fetcher.print_data(response)
                    print(fetcher.get_latitude_longitude(response))

                case "0":
                    break

                case _:
                    continue

        elif args["fetch"] == "all":
            city = input("Choose a city: ")
            response = fetcher.fetch_data(city)
            fetcher.print_data(response)
            coords = fetcher.get_latitude_longitude(response)
            print("latitude: ", coords[0])
            print("longitude: ", coords[1])

            response = airmass.get_airmass_region((math.floor(coords[0]) - 1, math.floor(coords[1]) - 1,
                                                   math.ceil(coords[0]) + 1, math.ceil(coords[1]) + 1))

            folder_name = "AIRMASS//"  # Donwload the files in a folder with the name of the product
            os.makedirs(folder_name, exist_ok=True)
            img_landing = folder_name + time.strftime("%Y_%m_%d-%H_%M_%S") + ".jpg"
            urllib.request.urlretrieve(response.url, img_landing)
            print("Image of Airmass was stored successfully!")
            break


if __name__ == "__main__":
    main()
