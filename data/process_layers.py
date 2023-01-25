layers = {
    "AIRMASS_RGB": "msg_fes:rgb_airmass",
    "CONVECTION_RGB": "msg_fes:rgb_convection",
    "DAY_MICROPHYSICS_RGB": "msg_fes:rgb_microphysics",
    "DUST_RGB": "msg_fes:rgb_dust",
    "FOG_LOW_CLOUDS_RGB": "msg_fes:rgb_fog",
    "SNOW_RGB": "msg_fes:rgb_snow",
    "EUROPEAN_HRV_RGB": "msg_fes:rgb_eview",
    "CLOUD_MASK": "msg_fes:clm",
    "CLOUD_TOP_HEIGHT": "msg_fes:cth"
}

INDEX_OFFSET = 1

import os
import time
import urllib

import requests
from pyproj import Proj, transform

from authentication import auth as auth
from coordinates import coordinates


def get_key_of_layer_by_index(index: int) -> str:
    return list(layers.keys())[index - INDEX_OFFSET]


def get_val_of_layer_by_index(index: int) -> str:
    return list(layers.values())[index - INDEX_OFFSET]


def print_layers() -> None:
    for count, key in enumerate(layers):
        print(f"{count + INDEX_OFFSET}. {key}")


def get_layer_region(coords: tuple, layer: str):
    access_token = auth.get_token()

    service_url = 'https://view.eumetsat.int/geoserver/ows?'

    # default layers
    land_layer = "backgrounds:ne_boundary_lines_land"
    coastline_layer = "backgrounds:ne_10m_coastline"
    countries_layer = "osmgray:ne_10m_admin_0_countries_points"
    provinces_layer = "osmgray:ne_10m_admin_1_states_provinces_lines"
    cities_layer = "osmgray:osm_places"

    format_option = 'image/jpeg'

    # Define region of interest
    projected_coords = get_projected_coords(coords)
    region_l = coordinates.coords_to_string(projected_coords)
    ratio = coordinates.calculate_ratio(projected_coords)

    # set the size of the image
    width = 1280

    # Create the request for RGB Airmass
    api_method = 'GetMap'
    payload = {'service': 'WMS',
               'access_token': access_token,
               'request': api_method,
               'version': '1.3.0',
               'layers': layer + "," + land_layer + "," + coastline_layer + "," + countries_layer + ","
                         + provinces_layer + "," + cities_layer,
               'format': format_option,
               'crs': 'EPSG:3857',
               'bbox': region_l,
               'width': width,
               'height': int(width * ratio)}
    return requests.get(service_url, params=payload)


def get_layer_image(layer: str, response=None):
    folder_name = layer + "//"  # Donwload the files in a folder with the name of the product
    os.makedirs(folder_name, exist_ok=True)
    img_landing = folder_name + time.strftime("%Y_%m_%d-%H_%M_%S") + ".jpg"
    urllib.request.urlretrieve(response.url, img_landing)
    print("\u001b[32mImage of " + layer + " was stored successfully!\u001b[0m")

    return img_landing


def get_projected_coords(coords) -> tuple:
    in_proj = Proj(init='epsg:4326')
    out_proj = Proj(init='epsg:3857')
    lat1, lon1 = coords[0], coords[1]
    proj_lat1, proj_lon1 = transform(in_proj, out_proj, lon1, lat1)
    lat2, lon2 = coords[2], coords[3]
    proj_lat2, proj_lon2 = transform(in_proj, out_proj, lon2, lat2)

    proj_coords = proj_lat1, proj_lon1, proj_lat2, proj_lon2

    return proj_coords
