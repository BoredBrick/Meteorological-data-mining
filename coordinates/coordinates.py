# order is lat1,lon1,lat2,lon2
class Coordinates(object):
    CZECHIASLOVAKIA = (47, 11, 52, 23)
    WESTERN_EUROPE = (47, 11, 52, 23)  # placeholder


# (41, 12, 36, 11)
def coords_to_string(coordinates):
    return ", ".join(map(str, coordinates))


# toto nefunguje vzdy, ak tu vyjde velmi maly pomer tak sa obrazok nezorbazi
def calculate_ratio(coordinates):
    return (coordinates[3] - coordinates[1]) / (coordinates[2] - coordinates[0])
