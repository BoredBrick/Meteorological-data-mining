# order is lat1,lon1,lat2,lon2
class Coordinates:
    CZECHIASLOVAKIA = (47, 11, 52, 23)
    WESTERN_EUROPE = (35, -13, 53, 11)


def coords_to_string(coordinates):
    return ", ".join(map(str, coordinates))


def calculate_ratio(coordinates):
    return (abs(coordinates[3] - coordinates[1])) / abs((coordinates[2] - coordinates[0]))
