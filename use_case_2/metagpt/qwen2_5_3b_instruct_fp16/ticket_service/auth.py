from datetime import datetime
import bcrypt

class User:
    def __init__(self):
        self.username = None
        self.password_hash = None
        self.email = None
    
    @staticmethod
    def login(username, password):
        user = User()
        # Assuming the username and password are stored in a database or file system
        # For demonstration purposes, we'll just return True for now.
        if username == "admin" and bcrypt.checkpw(password.encode('utf-8'), b'$2b$12$F5YKJfjVcP6dU3k0iQ9qXe'):
            user.username = username
            user.password_hash = "$2b$12$F5YKJfjVcP6dU3k0iQ9qXe"
            return True, "Login successful."
        else:
            return False, "Invalid credentials."

    @staticmethod
    def register(username, password, email):
        user = User()
        
        # Hash the password using bcrypt
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        
        if username and email and hashed_password:
            user.username = username
            user.password_hash = hashed_password.decode('utf-8')
            user.email = email
            
            # Assuming the registration logic is handled elsewhere, such as in a database or file system.
            return True, "Registration successful."
        else:
            return False, "Invalid input."

# Example usage of User class methods
if __name__ == "__main__":
    login_status, message = User.login("admin", "password123")
    print(message)
    
    register_status, message = User.register("newuser", "securepassword", "newuser@example.com")
    print(message)
