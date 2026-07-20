'''
File: sqlite3.py
Author: $USERNAME
Description: This file contains the class that interacts with the database and provides a way to store and retrieve data.
'''
import sqlite3
class SqliteDatabase():
    '''
    Class for interacting with a SQLite database.
    Attributes:
        connection: The connection object used to connect to the database.
        cursor: The cursor object used to execute SQL commands on the database.
    '''
    def __init__(self, database_file):
        '''
        Constructor for the SqliteDatabase class.
        Args:
            database_file: The file path of the SQLite database.
        '''
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()
    def execute_query(self, query):
        '''
        Executes a SQL query on the database.
        Args:
            query: The SQL query to be executed.
        '''
        return self.cursor.execute(query)
    def commit(self):
        '''
        Commits changes made to the database.
        '''
        self.connection.commit()
    def close(self):
        '''
        Closes the connection to the database.
        '''
        self.connection.close()