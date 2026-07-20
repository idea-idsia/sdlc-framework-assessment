# Authentication module
'''
This module handles user authentication.
'''
class Authenticator:
    def __init__(self):
        self.users = {}
    def add_user(self, username, password, role):
        self.users[username] = {'password': password, 'role': role}
    def login(self, username, password):
        if username in self.users and self.users[username]['password'] == password:
            return self.users[username]['role']
        else:
            return None