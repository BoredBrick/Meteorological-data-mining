import os
import time
import urllib.request
import warnings

from coordinates.coordinates import Coordinates
from data import fetch_data as fetcher
from data import process_airmass as airmass

warnings.simplefilter("ignore")
if __name__ == '__main__':

    print()
    print("[1] Fetch Airmass Data")
    print("[2] Fetch Other Data")
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
