# Program Demonstrating Encapsulation
class Student:
    def __init__(self):
        self.__marks = 85   # private variable

    def show_marks(self):
        print("Marks =", self.__marks)

s = Student()
s.show_marks()