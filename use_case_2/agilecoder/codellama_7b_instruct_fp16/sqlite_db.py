'''
sqlite_db.py
This file contains the SQLite database functions for the program.
'''
import sqlite3
from constants import CATEGORY_CHOICES
def create_ticket_table():
    # Create a new table in the database to store ticket information
    query = "CREATE TABLE tickets (id INTEGER PRIMARY KEY, description TEXT, category INT)"
    conn = sqlite3.connect("ticket_db.sqlite")
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
def create_user_table():
    # Create a new table in the database to store user information
    query = "CREATE TABLE users (username TEXT PRIMARY KEY, password TEXT)"
    conn = sqlite3.connect("ticket_db.sqlite")
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
def create_database():
    # Create a new database file and initialize the tables
    create_ticket_table()
    create_user_table()