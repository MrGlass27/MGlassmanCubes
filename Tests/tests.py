from form_collection import get_json
import sqlite3


def test_form_number():
    json_response = get_json()
    json_response = json_response['Entries']
    assert json_response >= 10



 def test_database_exists():
     name = 'cubes_database.db'
     connection = sqlite3.connect(name)
     cursor = connection.cursor()
     results = cursor.fetchall()
     cursor.close()
     connection.close()
     assert results != []
