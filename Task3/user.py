from datetime import datetime
class User:
    def __init__(self,user_id:int,name:str,surname:str,email:str,password:str,birthday:datetime):
        self.user_id = user_id
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.birthday = birthday

    def get_details(self):
        return f"Id: {self.user_id}, Name: {self.name}, Surname: {self.surname}, Email: {self.email}, Password: {self.password},Birthday: {self.birthday}"

    def get_age(self):
        return datetime.today().year - self.birthday.year

    def __repr__(self):
        return f"Id: {self.user_id}, Name: {self.name}, Surname: {self.surname}, Email: {self.email}, Password: {self.password},Birthday: {self.birthday}"

user = User(1233,'sa','das','dsad','fes',datetime(2006,4,4))

print(User.get_age(user))