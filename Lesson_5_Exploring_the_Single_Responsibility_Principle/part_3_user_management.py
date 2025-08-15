class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, username, password):
        self.users.append({"username": username, "password": password})
        print(f"User {username} added.")

    def authenticate(self, username, password):
        for user in self.users:
            if user['username'] == username and user['password'] == password:
                print(f"User {username} authenticated.")
                return True
        print("Authentication failed.")
        return False
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, username, password):
        self.users.append(User(username, password))
        print(f"User {username} added.")

class Authenticator:
    @staticmethod
    def authenticate(user_manager, username, password):
        for user in user_manager.users:
            if user.username == username and user.password == password:
                print(f"User {username} authenticated.")
                return True
        print("Authentication failed.")
        return False
