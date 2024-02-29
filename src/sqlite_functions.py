""" A set of functions that interact with the sqlite3 database."""
# Python imports
import sqlite3


def connect_to_database(database="data/patient_data.sqlite3", timeout=30.0):
    """Connect to the SQLite database.

    Args:
        database (str, optional) : The path to the SQLite database.
        timeout (float, optional) : sqlite3 connect timeout. Defaults to 30.

    Returns:
        sqlite_connection (database connection) : SQLite database connection.
    """

    print(f"Trying to connect to {database}...\n")

    sqlite_connection = sqlite3.connect(database, timeout=timeout)
    cursor = sqlite_connection.cursor()
    version_query = "select sqlite_version()"
    cursor.execute(version_query)
    version_record = cursor.fetchall()
    print(
        f"Connected to {database}!\n" f"SQLite Database Version is: {version_record}\n"
    )
    cursor.close()

    return sqlite_connection
