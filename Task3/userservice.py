class UserService:
    users = {}
    @classmethod
    def add_user(cls,user):
        if user.user_id in cls.users:
            return False
        cls.users[user.user_id] = user
        return True


    @classmethod
    def find_user(cls,user_id):
        if user_id in cls.users:
            return cls.users[user_id]
        else:
            print("No user found")


    @classmethod
    def delete_user(cls,user_id):
        if user_id in cls.users:
            del cls.users[user_id]
        else:
            print("Nu user found")

    @classmethod
    def update_user(cls,user_id,user_update):
        pass

    @classmethod
    def get_number(cls):
        return len(cls.users)


