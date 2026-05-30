# Program demonstrating constructor overloading
class Student:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)

s1 = Student()
s2 = Student("Rahul", 20)

s1.display()
s2.display()