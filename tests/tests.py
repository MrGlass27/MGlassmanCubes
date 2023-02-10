import sqlite3
import sys
import requests
from requests.auth import HTTPBasicAuth
from secrets import wufoo_key
from form_collection import url


def get_json():
    response = requests.get(url, auth=HTTPBasicAuth(wufoo_key, 'pass'))
    if response.status_code != 200:  # if we don't get an ok response we have trouble
        print(f"Failed to get data, response code:{response.status_code} and error message: {response.reason} ")
        sys.exit(-1)
    jsonresponse = response.json()
    return jsonresponse


def test_form_number():
    json_response = get_json()
    json_response = json_response['Entries']
    assert len(json_response) >= 10


def test_database_exists():
    name = 'cubes_database.db'
    connection = sqlite3.connect(name)
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS cubes_table (
                                       id INTEGER PRIMARY KEY,
                                       firstname text NOT NULL,
                                       lastname text NOT NULL,
                                       title text,
                                       organization text NOT NULL,
                                       email text NOT NULL,
                                       website text,
                                       phone text,
                                       opportunities text,
                                       time text,
                                       permission text
                                   ); ''')
    cursor.execute('''DELETE FROM cubes_table''')
    cursor.execute('''INSERT INTO cubes_table VALUES(?,?,?,?,?,?,?,?,?,?,?)''',
                   (1, 'matt', 'glass', 'lord', 'inc', 'gmail', 'website', 'cell', 'job', 'summer', 'yes'))
    results = cursor.execute("SELECT * from cubes_table").fetchall()
    assert results != []
