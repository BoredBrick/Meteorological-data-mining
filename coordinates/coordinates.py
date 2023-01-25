# order is lat1,lon1,lat2,lon2
coordinates = {
    "EUROPE": (34.975, -25.061, 71.801, 42.703),
    "CENTRAL_EUROPE": (45.012, 5.351, 55.383, 24.906),
    "EASTERN_EUROPE": (43.816, 19.366, 70.315, 57.379),
    "WESTERN_EUROPE": (40.702, -11.457, 61.620, 10.471),
    "NORTHERN_EUROPE": (54.325, -25.081, 71.552, 32.267),
    "SOUTHERN_EUROPE": (34.659, 6.319, 47.382, 27.039),
    "SOUTH-EASTERN_EUROPE": (39.340, 13.284, 48.546, 30.005),
    "SOUTH-WESTERN_EUROPE": (35.016, -11.010, 44.618, 5.074),

    "ALBANIA": (39.129, 18.943, 42.908, 21.360),
    "ANDORRA": (41.985, 1.043, 43.084, 2.208),
    "AUSTRIA": (46.160, 9.253, 49.259, 17.361),
    "BELARUS": (50.707, 22.768, 56.640, 33.205),
    "BELGIUM": (49.214, 2.318, 51.895, 6.624),
    "BOSNIA_AND_HERZEGOVINA": (42.249, 15.472, 45.567, 19.866),
    "BULGARIA": (41.019, 22.129, 44.469, 28.897),
    "CROATIA": (42.183, 13.318, 46.754, 19.559),
    "CYPRUS": (33.976, 31.742, 36.217, 35.104),
    "CZECH_REPUBLIC": (48.248, 11.846, 51.302, 19.185),
    "DENMARK": (54.072, 7.408, 58.224, 13.165),
    "ESTONIA": (57.079, 21.362, 60.155, 28.569),
    "FAROE_ISLANDS": (60.581, -8.344, 63.261, -5.268),
    "FINLAND": (58.797, 19.196, 70.553, 32.029),
    "FRANCE": (41.070, -5.262, 51.442, 9.855),
    "GERMANY": (47.017, 5.570, 55.323, 15.348),
    "GIBRALTAR": (35.650, -5.743, 36.282, -4.996),
    "GREECE": (34.515, 19.493, 42.139, 28.018),
    "GUERNSEY": (48.930, -2.875, 50.111, -1.526),
    "HUNGARY": (45.501, 15.933, 48.731, 23.096),
    "ICELAND": (62.251, -25.219, 67.832, -12.519),
    "IRELAND": (50.605, -11.728, 56.142, -5.268),
    "ITALY": (36.427, 6.309, 47.435, 18.746),
    "LATVIA": (55.365, 20.461, 58.332, 28.591),
    "LIECHTENSTEIN": (46.643, 9.041, 47.698, 10.206),
    "LITHUANIA": (53.564, 20.241, 56.816, 27.163),
    "LUXEMBOURG": (49.170, 5.548, 50.467, 6.756),
    "MACEDONIA": (40.623, 20.174, 42.601, 23.316),
    "MALTA": (35.245, 13.598, 36.564, 15.180),
    "MOLDOVA": (45.183, 26.437, 48.698, 30.348),
    "MONACO": (43.462, 7.149, 44.059, 7.741),
    "MONTENEGRO": (41.612, 18.152, 43.765, 20.547),
    "NETHERLANDS": (50.555, 3.307, 54.026, 7.679),
    "NORWAY": (57.237, 4.055, 71.651, 31.433),
    "POLAND": (48.730, 13.759, 55.431, 24.416),
    "PORTUGAL": (36.018, -10.672, 42.829, -5.685),
    "ROMANIA": (43.326, 20.042, 48.599, 30.303),
    "SAN_MARINO": (43.628, 12.106, 44.287, 13.226),
    "SERBIA": (41.656, 18.658, 46.358, 23.228),
    "SLOVAKIA": (47.457, 16.614, 49.852, 22.789),
    "SLOVENIA": (45.194, 13.187, 47.061, 16.702),
    "SPAIN": (35.687, -9.811, 44.191, 4.625),
    "SWEDEN": (54.667, 10.691, 69.740, 24.577),
    "SWITZERLAND": (45.435, 5.636, 48.072, 10.909),
    "UKRAINE": (44.106, 21.823, 52.741, 40.544),
    "UNITED_KINGDOM": (49.067, -8.344, 61.108, 2.422),
    "VATICAN": (41.736, 12.267, 42.066, 12.632)
}

INDEX_OFFSET = 1


def print_locations() -> None:
    for count, key in enumerate(coordinates):
        print(f"{count + INDEX_OFFSET}. {key}")


def get_val_of_location_by_index(index: int) -> tuple:
    return list(coordinates.values())[index - INDEX_OFFSET]


def coords_to_string(coordinates: tuple) -> str:
    return ", ".join(map(str, coordinates))


def calculate_ratio(coordinates: tuple) -> float:
    return abs(coordinates[3] - coordinates[1]) / abs(coordinates[2] - coordinates[0])
