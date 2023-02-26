import sqlite3
from sqlite3 import Error
from form_collection import get_json


def create_table(cursor):
    cursor.execute("""CREATE TABLE IF NOT EXISTS WuFooData(
    entryID INTEGER PRIMARY KEY,
    prefix TEXT NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    title TEXT,
    org TEXT,
    email TEXT,
    website TEXT,
    course_project BOOLEAN,
    guest_speaker BOOLEAN,
    site_visit BOOLEAN,
    job_shadow BOOLEAN,
    internship BOOLEAN,
    career_panel BOOLEAN,
    networking_event BOOLEAN,
    subject_area TEXT NOT NULL,
    description TEXT,
    funding BOOLEAN,
    created_date TEXT,
    created_by TEXT);""")
    cursor.execute('''DELETE FROM cubes_table''')


def push_to_table(info, cursor):
    # the insert or ignore syntax will insert if the primary key isn't in use or ignore if the primary key is in the DB
    insert_statement = """INSERT OR IGNORE INTO WuFooData (entryID, prefix, first_name, last_name, title, org, email, 
    website,course_project, guest_speaker, site_visit, job_shadow, internship, career_panel, networking_event,
    subject_area, description, funding, created_date, created_by) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
    for entry in info:
        entry_values = list(
            entry.values()
        )  # get the list of values from the dictionary
        entry_values[0] = int(
            entry_values[0]
        )  # the EntryID is a string, but I want it to be a number
        entry_values = entry_values[:-2]
        cursor.execute(insert_statement, entry_values)


def database_setup():
    json_response = get_json()
    json_response = json_response['Entries']
    connection = None

    try:
        name = 'cubes_database.db'
        connection = sqlite3.connect(name)
        cursor = connection.cursor()
        create_table(cursor)
        push_to_table(json_response, cursor)
        connection.commit()
        cursor.close()
    except Error as e:
        print(f'A Database Error has occurred: {e}')
    finally:
        if connection:
            connection.close()
            print('Database connection closed.')
    return json_response


database_setup()
