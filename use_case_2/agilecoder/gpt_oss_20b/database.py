'''
Database singleton managing SQLite connection and schema.
'''
import sqlite3
from typing import Any, List, Tuple
from config import DATABASE_FILE
class Database:
    _instance = None
    def __init__(self):
        self.conn = sqlite3.connect(DATABASE_FILE, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self._create_tables()
    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    def _create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tickets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT NOT NULL,
                category TEXT NOT NULL,
                status TEXT NOT NULL,
                opening_date TEXT NOT NOT NULL,
                last_mod_date TEXT NOT NULL,
                closing_date TEXT,
                created_by_role TEXT NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ticket_id INTEGER NOT NULL,
                role TEXT NOT NULL,
                message TEXT NOT NULL,
                timestamp TEXT NOT NULL,
                FOREIGN KEY(ticket_id) REFERENCES tickets(id)
            )
        ''')
        self.conn.commit()
    def execute(self, sql: str, params: Tuple = (), fetch: bool = False) -> List[sqlite3.Row]:
        cur = self.conn.cursor()
        cur.execute(sql, params)
        self.conn.commit()
        if fetch:
            return cur.fetchall()
        return []
    def query(self, sql: str, params: Tuple = ()) -> List[sqlite3.Row]:
        cur = self.conn.cursor()
        cur.execute(sql, params)
        return cur.fetchall()