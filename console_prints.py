from coordinates.coordinates import print_locations
from data.process_layers import *


def print_intro():
    print("\n\u001b[36;1m---------------------------------------------------------")
    print("  A script for mining meteorological data from websites")
    print("---------------------------------------------------------\n \u001b[0m ")


def select_fetching() -> str:
    print("\u001b[36m[1]\u001b[37m Fetch satellite images for a LOCATION\u001b[0m")
    print("\u001b[36m[2]\u001b[37m Fetch satellite images for a CITY\u001b[0m")
    print("\u001b[36m[3]\u001b[37m Fetch meteorological data for a CITY\u001b[0m")
    print("\u001b[36m[4]\u001b[37m Fetch meteorological data and satellite images for a CITY\u001b[0m")
    print("\u001b[36m[0]\u001b[37m Quit application\u001b[0m")
    option = input("\u001b[35mChoose an option:\u001b[0m ")
    print()
    return option


def is_endless_fetching() -> bool:
    print("\u001b[36m[1]\u001b[37m Endless fetching\u001b[0m")
    print("\u001b[36m[2]\u001b[37m One-time fetch\u001b[0m")

    while True:
        option = input("\u001b[35mChoose an option:\u001b[0m ")
        match option:
            case "1":
                print()
                return True
            case "2":
                print()
                return False
            case _:
                print("Invalid option. Please choose a valid option.")


def select_layer() -> str:
    print_layers()
    layer = input("\u001b[35mChoose index of layer:\u001b[0m ")
    print()
    return layer


def select_location() -> str:
    print_locations()
    location = input("\u001b[35mChoose index of location:\u001b[0m ")
    print()
    return location


def select_city() -> str:
    city = input("\u001b[35mChoose a city:\u001b[0m ")
    print()
    return city.strip()


def select_endless_fetching() -> str:
    print("\u001b[36m[1]\u001b[37m Fetch once\u001b[0m")
    print("\u001b[36m[2]\u001b[37m Endless fetching\u001b[0m")
    fetching = input("\u001b[35mChoose an option:\u001b[0m ")
    print()
    return fetching
