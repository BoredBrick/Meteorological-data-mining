import argparse
import os
import sys
import time
import urllib.request
import warnings
import math

from coordinates.coordinates import Coordinates
from data import fetch_data as fetcher
from data import process_airmass as airmass

warnings.simplefilter("ignore")
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--fetch", required=False, help="all - start fetching all possible data")
    args = vars(ap.parse_args())

    wasEnd = False

    while not wasEnd:

        if len(sys.argv) < 2:
            print()
            print("[1] Fetch Airmass Data")
            print("[2] Fetch Other Data")
            print("[0] Quit application")
            option = input("Choose an option: ")

            if option == "1":
                response = airmass.get_airmass_region(Coordinates.WESTERN_EUROPE)

                f1 = urllib.request.urlopen(response.url)  # create file-like objects from urls

                folder_name = "AIRMASS//"  # Donwload the files in a folder with the name of the product
                os.makedirs(folder_name, exist_ok=True)
                img_landing = folder_name + time.strftime("%Y_%m_%d-%H_%M_%S") + ".jpg"
                urllib.request.urlretrieve(response.url, img_landing)
                print("Image of Airmass was stored successfully!")

            if option == "2":
                city = input("Choose a city: ")
                response = fetcher.fetch_data(city)
                fetcher.print_data(response)
                print(fetcher.get_latitude_longitude(response))

            if option == "0":
                wasEnd = True

        if (args["fetch"] == "all"):
            city = input("Choose a city: ")
            response = fetcher.fetch_data(city)
            fetcher.print_data(response)
            coords = fetcher.get_latitude_longitude(response)
            print("latitude: ", coords[0])
            print("longitude: ", coords[1])

            response = airmass.get_airmass_region((math.floor(coords[0]) - 1, math.floor(coords[1]) - 1, math.ceil(coords[0]) + 1, math.ceil(coords[1]) + 1))

            f1 = urllib.request.urlopen(response.url)  # create file-like objects from urls

            folder_name = "AIRMASS//"  # Donwload the files in a folder with the name of the product
            os.makedirs(folder_name, exist_ok=True)
            img_landing = folder_name + time.strftime("%Y_%m_%d-%H_%M_%S") + ".jpg"
            urllib.request.urlretrieve(response.url, img_landing)
            print("Image of Airmass was stored successfully!")

            wasEnd = True

if __name__ == "__main__":
    main()
