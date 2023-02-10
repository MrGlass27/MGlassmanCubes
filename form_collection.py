import sys
import requests
from requests.auth import HTTPBasicAuth
from secrets import wufoo_key


# call API to get json data of form entries
url = "https://mrglass27.wufoo.com/api/v3/forms/zse7wqw1sji2tk/entries/json"


def get_json():
    response = requests.get(url, auth=HTTPBasicAuth(wufoo_key, 'pass'))
    if response.status_code != 200:  # if we don't get an ok response we have trouble
        print(f"Failed to get data, response code:{response.status_code} and error message: {response.reason} ")
        sys.exit(-1)
    jsonresponse = response.json()
    return jsonresponse
