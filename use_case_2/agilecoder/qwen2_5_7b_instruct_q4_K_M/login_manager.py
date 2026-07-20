"""
Manages user authentication with secure password hashing.
"""
import hashlib
class LoginManager:
    def __init__(self):
        self.users = {
            "user1": "5f4dcc3b5aa765d61d8327deb882cf99",  # SHA-256 hash of 'pass1'
            "staff1": "c4ca4238a0b923820dcc509a6f75849b"   # SHA-256 hash of 'pass2'
        }
    def authenticate_user(self, username: str, password: str) -> bool:
        if username not in self.users:
            return False
        stored_hash = self.users[username]
        new_hash = hashlib.sha256(password.encode()).hexdigest()
        return stored_hash == new_hash
    def get_user_role(self, username: str) -> str:
        roles = {
            "user1": 'user',
            "staff1": 'staff'
        }
        return roles.get(username)