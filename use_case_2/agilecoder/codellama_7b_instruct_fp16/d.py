'''
File: d.py
Author: $USERNAME
Description: $DESCRIPTION
'''
from pymongo import MongoClient
class Database:
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["ticket_management"]
    def connect(self, host, port):
        pass
    def execute(self, query):
        pass
    def close(self):
        pass