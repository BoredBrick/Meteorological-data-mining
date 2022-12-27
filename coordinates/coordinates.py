# order is lat1,lon1,lat2,lon2
coordinates = {
    "CZECHIASLOVAKIA": (47, 11, 52, 23),
    "WESTERN_EUROPE": (35, -13, 53, 11),
    "TEST": (1, 2, 3, 4)
}

INDEX_OFFSET = 1


def print_locations():
    for count, key in enumerate(coordinates):
        print(f"{count + INDEX_OFFSET}. {key}")


def get_val_by_index(index: int):
    return list(coordinates.values())[index - INDEX_OFFSET]


def coords_to_string(coordinates: tuple) -> str:
    return ", ".join(map(str, coordinates))


def calculate_ratio(coordinates: tuple):
    return (abs(coordinates[3] - coordinates[1])) / abs((coordinates[2] - coordinates[0]))
