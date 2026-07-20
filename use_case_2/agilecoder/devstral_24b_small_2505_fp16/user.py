'''
User Class.
'''
import sqlite3
class User:
    def __init__(self, username, role="user"):
        self.username = username
        self.role = role
    def create_ticket(self, db_manager, title, description, category):
        if self.role == "admin" or self.role == "helpdesk" or self.role == "simple_user":
            db_manager.add_ticket(title, description, category)
            return True
        else:
            print("Permission denied")
            return False
    def modify_ticket(self, db_manager, ticket_id, new_title, new_description):
        if self.role == "admin" or self.role == "helpdesk" or self.role == "simple_user":
            db_manager.modify_ticket(ticket_id, new_title, new_description)
            return True
        else:
            print("Permission denied")
            return False
    def change_ticket_status(self, db_manager, ticket_id, status):
        if self.role == "admin" or self.role == "helpdesk":
            try:
                cursor = db_manager.conn.cursor()
                query = 'UPDATE tickets SET status=?, last_modified_at=CURRENT_TIMESTAMP WHERE id=?'
                cursor.execute(query, (status, ticket_id))
                db_manager.conn.commit()
                return True
            except sqlite3.Error as e:
                print(f"Database error: {e}")
                return False
        else:
            print("Permission denied")
            return False
    def add_message(self, db_manager, ticket_id, message):
        try:
            cursor = db_manager.conn.cursor()
            query = 'INSERT INTO messages (ticket_id, message) VALUES (?, ?)'
            cursor.execute(query, (ticket_id, message))
            db_manager.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return False
    def get_messages(self, db_manager, ticket_id):
        try:
            cursor = db_manager.conn.cursor()
            query = 'SELECT * FROM messages WHERE ticket_id=?'
            cursor.execute(query, (ticket_id,))
            results = cursor.fetchall()
            return results
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []