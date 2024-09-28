from models.user import User

class UserDAO:
    def __init__(self):
        self.users = {}

    def create_user(self, user: User):
        self.users[user.id] = user
    
    def get_user(self, id: int):
        if id in self.users:
            return self.users.get(id)
        else:
            raise Exception('User not found')
    
    def get_all_users(self):
        return list(self.users.values())
    
    def update_user(self, user: User):
        if user.id in self.users:
            self.users[user.id] = user
            return user
        return None

    def delete_user(self, id: int):
        if id in self.users:
            return self.users.pop(id)
        return None