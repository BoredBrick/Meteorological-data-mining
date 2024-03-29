import json
import os
import sys
import warnings

import requests

from authentication import credentials


def get_token() -> str:
    sys.path.append(os.path.dirname(os.getcwd()))
    warnings.simplefilter("ignore")
    access_token = generate_token(eumetsat_consumer_key=credentials.eumetsat_consumer_key,
                                  eumetsat_consumer_secret=credentials.eumetsat_consumer_secret)
    return access_token


# ---------------------------------------------------------------------------

def generate_token(apis_endpoint="https://api.eumetsat.int",
                   eumetsat_consumer_key=None, eumetsat_consumer_secret=None,
                   credentials_file=None, token_url=None):
    '''
    Function to generate an access token for interacting with EUMETSAT Data
    Service APIs

    Args:
        apis_endpoint (str):    The endpoint URL of the API
        eumetsat_consumer_key (str):     The consumer key as a string
        eumetsat_consumer_secret (str):  The consumer secret as a string.
        credentials_file (str): An optional json format credentials file
        token_url (str):        The token URL (if different from default)

    Returns:
        An access token (if pass) or None (if fail).
    '''

    # build the token URL:
    if not token_url:
        token_url = apis_endpoint + "/token"

    # check the credentials.
    if not credentials_file and not eumetsat_consumer_key:
        print('No consumer key or credentials file given. Quitting...')
        return None

    if credentials_file:
        with open(credentials_file) as f:
            data = json.load(f)
            eumetsat_consumer_key = data['eumetsat_consumer_key']
            eumetsat_consumer_secret = data['eumetsat_consumer_secret']

    response = requests.post(
        token_url,
        auth=requests.auth.HTTPBasicAuth(eumetsat_consumer_key, eumetsat_consumer_secret),
        data={'grant_type': 'client_credentials'},
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )

    assert_response(response)
    return response.json()['access_token']


# ---------------------------------------------------------------------------

def assert_response(response, success_code=200):
    '''
    Function to check API key generation response. Will return an error
    if the key retrieval was not successful.

    Args:
        response (obj):      The authentication response.
        success_code (int):  The expected success code (200).

    Returns:
        Nothing if success, error message if failed.
    '''

    assert response.status_code == success_code, \
        "API Request Failed: {}\n{}".format(response.status_code,
                                            response.content)
