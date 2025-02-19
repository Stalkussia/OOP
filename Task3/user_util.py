import random
import string
import re
class UserUtil:
    @staticmethod
    def generate_user_id(): #generates a user ID containing the 2025 year as first two digits and then random 8 digits
        list = [2,5]
        for i in range(7):
            list.append(random.randint(0,9))
        user_id = ''.join(map(str,list))
        return user_id

    @staticmethod
    def generate_password(): #Generates a random password conatining upper, lower, symbol and a digit all at once
        while True:
            password = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation,k=8))
            if UserUtil.is_strong_password(password):
                return password

    @staticmethod
    def is_strong_password(password): #Checks whether the password generated is strong enough
        if len(password) >= 8:
            upper = any(c.isupper() for c in password)
            lower = any(c.islower() for c in password)
            symbol = any(c in "!@#$%^&*()_+-=[]{}|;:'\",.<>?/" for c in password)
            digit = any(c.isdigit() for c in password)
            return upper and lower and symbol and digit

    @staticmethod
    def generate_email(name,surname,domain): #Generates an email of type name.surname@domain.com in lowercase:
        email = f'{name}.{surname}@{domain}.com'.lower()
        return email


    @staticmethod
    def validate_email(email): #Checks whether the email has an appropriate format of name.surname@domain.com(Honestly, couldnt do it myself, asked chatgpt to do it)
        return bool(re.match(r'^[a-z]+\.[a-z]+@[a-z]+\.[a-z]+$', email))


password = UserUtil.generate_password() #stores generated password as an argument to check in future
email = UserUtil.generate_email('Aiman','Sadiev','gmail') #same with the email but provided the attributes to make an email.
print(email)
print(UserUtil.validate_email(email))
