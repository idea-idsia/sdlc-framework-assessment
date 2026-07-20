'''
File: database.py
Author: $USERNAME
Description: This file contains the class that represents a database used by the ticket management system.
'''
import sqlite3
class Database():
    '''
    Class for representing a database used by the ticket management system.
    Attributes:
        tms: The TicketManagementSystem object that provides access to the database and other functionalities.
        sqlite_db: The SqliteDatabase object used to interact with the database.
    '''
    def __init__(self, tms):
        '''
        Constructor for the Database class.
        Args:
            tms: The TicketManagementSystem object that provides access to the database and other functionalities.
        '''
        self.tms = tms
        self.sqlite_db = sqlite3.connect("tickets.db", check_same_thread=False)
    def execute_query(self, query):
        '''
        Executes a query on the SQL database.
        Args:
            query: The SQL query to execute.
        Returns:
            The result of the query as a list of dictionaries.
        '''
        cursor = self.sqlite_db.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    def close(self):
        '''
        Closes the SQL database connection.
        '''
        self.sqlite_db.close()