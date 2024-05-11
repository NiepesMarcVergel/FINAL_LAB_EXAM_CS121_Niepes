import os
from Utils.user import User

class UserManager:
    def __init__(self):
        self.users = []

    def register(self, username, password):
        if self.validate_username(username) and self.validate_password(password):
            user = User(username, password)
            self.users.append(user)
            self.save_users()
            return True
        return False

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                return user
        return None

    def validate_username(self, username):
        return len(username) >= 4

    def validate_password(self, password):
        return len(password) >= 8

    def save_users(self):
        if not os.path.exists('data'):
            os.makedirs('data')
        with open('data/users.txt', 'w') as f:
            for user in self.users:
                f.write(f"{user.username},{user.password}\n")

    def load_users(self):
        if not os.path.exists('data'):
            os.makedirs('data')
        if os.path.exists('data/users.txt'):
            with open('data/users.txt', 'r') as f:
                for line in f.readlines():
                    username, password = line.strip().split(',')
                    self.users.append(User(username, password))