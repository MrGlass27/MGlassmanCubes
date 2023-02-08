import configparser
import requests
import sys
from requests.auth import HTTPBasicAuth


# gets apikey from config file
# comment to test workflow
def get_apikey():
    config = configparser.ConfigParser()
    config.read('app.config')
    apikey_from_file = config['secrets']['apikey']
    return apikey_from_file


# get form identifier from config file
def get_identifier():
    config = configparser.ConfigParser()
    config.read('app.config')
    identifier_from_file = config['secrets']['identifier']
    return identifier_from_file


# get subdomain from config file
def get_subdomain():
    config = configparser.ConfigParser()
    config.read('app.config')
    subdomain_from_file = config['secrets']['subdomain']
    return subdomain_from_file


# call API to get json data of form entries
url = "https://{}.wufoo.com/api/v3/forms/{}/entries/json".format(get_subdomain(), get_identifier())


def get_json() -> dict:
    response = requests.get(url, auth=HTTPBasicAuth(get_apikey(), 'pass'))
    if response.status_code != 200:  # if we don't get an ok response we have trouble
        print(f"Failed to get data, response code:{response.status_code} and error message: {response.reason} ")
        sys.exit(-1)
    jsonresponse = response.json()
    return jsonresponse