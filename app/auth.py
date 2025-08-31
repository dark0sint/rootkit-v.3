# app/auth.py

class Auth:
    def __init__(self):
        # Simulasi database user: username -> password
        self.users = {
            "admin": "admin123",
            "user1": "password1"
        }
        self.logged_in_user = None

    def login(self, username, password):
        if username in self.users and self.users[username] == password:
            self.logged_in_user = username
            return True
        return False

    def logout(self):
        self.logged_in_user = None

    def is_authenticated(self):
        return self.logged_in_user is not None

    def get_current_user(self):
        return self.logged_in_user
