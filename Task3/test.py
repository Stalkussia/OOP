import unittest
from datetime import datetime
from userservice import UserService
from user import User
from user_util import UserUtil

#The file to test all the classes made. Tried my best to do it fully myself but somewhere asked chatgpt to help

class TestUser(unittest.TestCase): #Creating a class to test User class with unittest
    def test_user(self):
        user = User(230121026,'Aiman','Sadiev','aiman.sadiev@alatoo.edu.kg','qwerty',datetime(2006,4,4)) #providing a test user attribute
        self.assertEqual(user.name, 'Aiman') #checks and returns boolean if user.name and provided name are equal
        self.assertEqual(user.surname, 'Sadiev') #Same with the surname and user.surname
        self.assertTrue("@alatoo.edu.kg" in user.email) #checks if @alatoo.edu.kg is in user.email

    def test_get_age(self):
        user = User(230121026, 'Aiman', 'Sadiev', 'aiman.sadiev@alatoo.edu.kg', 'qwerty',datetime(2006,4,4))
        self.assertTrue(user.get_age() > 0) #checks if the age is greater than 0


class TestUserService(unittest.TestCase):
    def test_add_find_user(self):
        user = User(230121026, 'Aiman', 'Sadiev', 'aiman.sadiev@alatoo.edu.kg', 'qwerty',datetime(2006,4,4))
        UserService.add_user(user) #adding the user to users list
        self.assertEqual(UserService.find_user(230121026), user) #Checking if it could find the user in the dictionary

    def test_delete_user(self):
        user = User(230121026, 'Aiman', 'Sadiev', 'aiman.sadiev@alatoo.edu.kg', 'qwerty',datetime(2006,4,4))
        UserService.add_user(user)
        UserService.delete_user(230121026) #deletes the user from the dictionary
        self.assertIsNone(UserService.find_user(230121026)) #checks if the output is NOne as we try to find deleted user


class TestUserUtil(unittest.TestCase): #Creating a class to test User Util class
    def test_generate_user_id(self):
        user_id = UserUtil.generate_user_id() # Creating a user id
        self.assertEqual(len(str(user_id)), 9) #Checks if the length is appropriate

    def test_generate_password(self):
        password = UserUtil.generate_password() #generates password
        self.assertTrue(UserUtil.is_strong_password(password)) #Checks if password is strong enough

    def test_validate_email(self):
        self.assertTrue(UserUtil.validate_email("aiman.sadiev@gmail.com")) #the email is appropriate so we expect True
        self.assertFalse(UserUtil.validate_email("aiman@gmail.com")) #The email does not contain surname a dot between them and dots in the domain so the output should be False


if __name__ == "__main__":
    unittest.main()
