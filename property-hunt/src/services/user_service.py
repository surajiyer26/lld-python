from dao.user_dao import UserDAO
from models.user import User

user_dao = UserDAO()

class UserService:
    def __init__(self):
        self.user_dao = user_dao

    def add_user(self, user: User):
        return self.user_dao.create_user(user)
    
    def get_user(self, id: int):
        return self.user_dao.get_user(id)
    
    def list_all_users(self):
        return self.user_dao.get_all_users()
    
    def update_user(self, user: User):
        return self.user_dao.update_user(user)

    def remove_user(self, id: int):
        return self.user_dao.delete_user(id)