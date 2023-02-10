from form_collection import get_json
from db_setup import push_to_table
import sqlite3


def test_form_number():
    json_response = get_json()
    json_response = json_response['Entries']
    assert len(json_response) >= 10


def test_database_exists():
    json_response = get_json()
    json_response = json_response['Entries']
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
    push_to_table(json_response, cursor)
    results = cursor.execute("SELECT * from cubes_table").fetchall()
    assert results != []
