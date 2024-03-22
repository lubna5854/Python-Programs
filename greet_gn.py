class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Greet_Person(Person):
    def greet(self):
        print(f"Hello! I am {self.name} years old and my gender is {self.age}.")

person1 = Greet_Person(name="Lubna",age=30)
person1.greet()


""" 
class Teacher:

    def greet(self,uname,age):

        print(f"Hello! I am {uname} and I am {age} years old ")

teacher=Teacher()
teacher.greet("Lubna",32)
"""