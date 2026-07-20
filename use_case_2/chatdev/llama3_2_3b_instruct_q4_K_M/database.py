import sqlite3
from user import UserClass  # Import User class from user module
class Database:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
    # ... rest of the methods ...