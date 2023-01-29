from coordinates.coordinates import print_locations
from data.process_layers import *


def print_intro():
    print("\n\u001b[36;1m---------------------------------------------------------")
    print("  A script for mining meteorological data from websites")
    print("---------------------------------------------------------\n \u001b[0m ")


def select_fetching() -> str:
    print_intro()
    print("\u001b[36m[1]\u001b[37m Fetch Meteorological Satellite Images\u001b[0m")
    print("\u001b[36m[2]\u001b[37m Fetch Meteorological Data\u001b[0m")
    print("\u001b[36m[0]\u001b[37m Quit Application\u001b[0m")
    option = input("\u001b[35mChoose an option:\u001b[0m ")
    print()
    return option


def select_all_fetching() -> str:
    print_intro()
    print("\u001b[36m[1]\u001b[37m Fetch Data For Location\u001b[0m")
    print("\u001b[36m[2]\u001b[37m Fetch Data For City\u001b[0m")
    print("\u001b[36m[0]\u001b[37m Quit application\u001b[0m")
    option = input("\u001b[35mChoose an option:\u001b[0m ")
    print()
    return option


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
    return city


def select_endless_fetching() -> str:
    print("\u001b[36m[1]\u001b[37m Fetch once\u001b[0m")
    print("\u001b[36m[2]\u001b[37m Endless fetching\u001b[0m")
    fetching = input("\u001b[35mChoose an option:\u001b[0m ")
    print()
    return fetching
