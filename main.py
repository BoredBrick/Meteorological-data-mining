import time
import warnings

from console_prints import *
from data.process_data import fetch_and_process_data

warnings.simplefilter("ignore")

layer_update_time = 10 * 60


def main():
    print_intro()
    endless_fetching = is_endless_fetching()
    selected_layer = None
    selected_location = None
    selected_city = None
    while True:

        while True:
            try:
                option = int(select_fetching())
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer option.")
        match option:
            case 1:
                selected_layer = select_layer()
                selected_location = select_location() if option == 1 else select_city()
            case 2:
                selected_layer = select_layer()
                selected_city = select_city()
            case 3 | 4:
                selected_city = select_city()
                if option == 4:
                    selected_layer = select_layer()

            case 0:
                break

            case _:
                continue

        if endless_fetching:
            while True:
                fetch_and_process_data(option, selected_layer, selected_location, selected_city)
                try:
                    time.sleep(layer_update_time)
                except KeyboardInterrupt:
                    break
        else:
            fetch_and_process_data(option, selected_layer, selected_location, selected_city)


if __name__ == "__main__":
    main()
