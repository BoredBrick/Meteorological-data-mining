# import cv2
from datetime import date
import os
import sys
import ssl
import warnings
import requests
import urllib.request
from IPython.core.display import HTML
from IPython.display import Image
import matplotlib.pyplot as plt
from owslib.wms import WebMapService
from owslib.util import Authentication
from authentification import authentification as auth

warnings.simplefilter("ignore")
if __name__ == '__main__':
    ssl._create_default_https_context = ssl._create_unverified_context
    sys.path.append(os.path.dirname(os.getcwd()))
    warnings.simplefilter("ignore")
    route: str = os.getcwd()
    print(os.path.join(os.path.dirname(str(os.getcwd())), 'authentification', 'credentials.json'))
    credentials = auth.import_credentials(
        os.path.join(str(os.getcwd()), 'authentification', 'credentials.json'))
    access_token = auth.generate_token(consumer_key=credentials['consumer_key'],
                                       consumer_secret=credentials['consumer_secret'])
    print('Access token retrieved: ' + access_token)

    # We access the WMS service using the following API end-point URL
    service_url = 'https://view.eumetsat.int/geoserver/ows?'
    wms = WebMapService(service_url, auth=Authentication(verify=False))

    # Get the list of all available layers
    for item in list(wms.contents):
        print(item)

    target_layer = "msg_fes:rgb_airmass"

    # We can interrogate one of the layers to see what properties it has...
    #display(HTML('<b>Layer title: </b>' + str(wms[target_layer].title)))
    #display(HTML('<b>CRS options: </b>' + str(wms[target_layer].crsOptions)))
    #display(HTML('<b>Bounding box: </b>' + str(wms[target_layer].boundingBox)))
    #display(HTML('<b>Layer abstract: </b>' + str(wms[target_layer].abstract)))
    #display(HTML('<b>Timestamp: </b>' + str(wms[target_layer].timepositions)))  # by default WMS will return themost recent image



    API_method = 'GetMap'

    # check available format options
    for iter_format_option in wms.getOperationByName(API_method).formatOptions:
        print("Format option: ", iter_format_option)

    # select format option
    format_option = 'image/jpeg'

    # Define region of interest
    # region_l = "30,-10,45,10"  # order is lat1,lon1,lat2,lon2
    region_l = "45,11,52,23"  # Czechoslovakia

    # set the size of the image
    xval = 1200
    region = [int(x) for x in region_l.split(",")]
    ratio = (region[3] - region[1]) / (region[2] - region[0])

    # Set the date and time
    tt = "2021-01-11T12:00:00.000Z"

    # Create the request for RGB Airmass
    payload = {'service': 'WMS',
               'access_token': access_token,
               'request': 'GetMap',
               'version': '1.3.0',
               'layers': target_layer + ",backgrounds:ne_boundary_lines_land",
               # the layer is displayed together with the coastlines layer
               'format': format_option,
               'crs': 'EPSG:4326',
               'bbox': region_l,
               'width': int(xval),
               'height': int(xval / ratio)}
    req1 = requests.get(service_url, params=payload)

    # Display the two images side by side (using matplotlib)
    NUM_ROWS = 1
    IMGs_IN_ROW = 2
    f, ax = plt.subplots(NUM_ROWS, IMGs_IN_ROW, figsize=(15, 6))

    f1 = urllib.request.urlopen(req1.url)  # create file-like objects from urls
    a = plt.imread(f1, 0)  # read the images file in a numpy array

    ax[0].imshow(a)
    ax[0].set_title('Airmass RGB')
    title = 'AIRMASS IN CZECHOSLOVAKIA, ', date.today()
    f.suptitle(title, fontsize=20, y=1.05)
    plt.tight_layout()
    plt.show()

    payload = {'service': 'WMS',
               'access_token': access_token,
               'request': 'GetMap',
               'version': '1.3.0',
               'layers': target_layer + ",backgrounds:ne_boundary_lines_land",
               # the layer is displayed together with the coastlines layer
               'format': format_option,
               'crs': 'EPSG:4326',
               'bbox': region_l,
               'width': int(xval),
               'height': int(xval / ratio)}
    req1 = requests.get(service_url, params=payload)

    folder_name = "_DOWNLOAD//"  # Donwload the files in a folder with the name of the product
    os.makedirs(folder_name, exist_ok=True)
    img_landing = folder_name + "prod.jpg".replace(':', '-')
    urllib.request.urlretrieve(req1.url, img_landing)
