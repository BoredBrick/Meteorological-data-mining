import requests

from authentification import authentification as auth
from coordinates import coordinates


def get_airmass_region(coords):
    access_token = auth.get_token()

    service_url = 'https://view.eumetsat.int/geoserver/ows?'

    target_layer = "msg_fes:rgb_airmass"
    format_option = 'image/jpeg'

    # Define region of interest
    region_l = coordinates.coords_to_string(coords)

    # set the size of the image
    width = 1200
    ratio = coordinates.calculate_ratio(coords)

    # Create the request for RGB Airmass
    api_method = 'GetMap'
    payload = {'service': 'WMS',
               'access_token': access_token,
               'request': api_method,
               'version': '1.3.0',
               'layers': target_layer + ",backgrounds:ne_boundary_lines_land",
               'format': format_option,
               'crs': 'EPSG:4326',
               'bbox': region_l,
               'width': width,
               'height': int(width / ratio)}
    return requests.get(service_url, params=payload)
