class Person:
    #Constructors
    def __init__(self,name,surname,age = None, gender = None):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender
    #methods
    def walk(self):
        print("Person", self.name, "is walking")

    def info(self):
        print('Person name is', self.name, "surname is ", self.surname, "age is ", self.age, "gender is ", self.gender)

