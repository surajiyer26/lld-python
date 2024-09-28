class User:
    def __init__(self, id: int, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email

    def __str__(self):  
        return f'User {self.name} ({self.email} with id {self.id})'