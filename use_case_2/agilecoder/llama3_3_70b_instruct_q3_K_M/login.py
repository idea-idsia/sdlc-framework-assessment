'''
The Login class that handles user authentication.
'''
import bcrypt
class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    def authenticate(self, db):
        try:
            # Authentication logic
            cursor = db.cursor()
            cursor.execute("SELECT * FROM users WHERE username=?", (self.username,))
            user = cursor.fetchone()
            if user:
                stored_password = user[2]  # Assuming the password is the third column
                if bcrypt.checkpw(self.password.encode('utf-8'), stored_password):
                    return True
            return False
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return False