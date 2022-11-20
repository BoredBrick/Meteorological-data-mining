import os
import time
import urllib.request
import warnings
from datetime import date

import matplotlib.pyplot as plt

from data import process_airmass as airmass
from data import fetch_data as fetcher

warnings.simplefilter("ignore")
if __name__ == '__main__':

    print()
    print("[1] Fetch Airmass Data")
    print("[2] Fetch Other Data")
    option = input("Choose an option: ")

    if (option == "1"):
        response = airmass.get_airmass_region(45, 11, 52, 23)

        NUM_ROWS = 1
        IMGs_IN_ROW = 2
        f, ax = plt.subplots(NUM_ROWS, IMGs_IN_ROW, figsize=(15, 6))

        f1 = urllib.request.urlopen(response.url)  # create file-like objects from urls
        a = plt.imread(f1, 0)  # read the images file in a numpy array

        # SHOW DOWNLOADED IMAGE (we don't need that now)
        # ax[0].imshow(a)
        # ax[0].set_title('Airmass RGB')
        # title = 'AIRMASS IN CZECHOSLOVAKIA, ', date.today()
        # f.suptitle(title, fontsize=20, y=1.05)
        # plt.tight_layout()
        # plt.show()

        folder_name = "AIRMASS//"  # Donwload the files in a folder with the name of the product
        os.makedirs(folder_name, exist_ok=True)
        img_landing = folder_name + time.strftime("%Y_%m_%d-%H_%M_%S") + ".jpg"
        urllib.request.urlretrieve(response.url, img_landing)
        print("Image of Airmass was stored succesfully!")

    if (option == "2"):
        city = input("Choose a city: ")
        response = fetcher.fetch_data(city)
        fetcher.print_data(response)


