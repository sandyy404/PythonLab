# Program demonstrating getter and setter methods.
class Student:
    def __init__(self):
        self.__marks = 0
    def set_marks(self, m):
        self.__marks = m
    def get_marks(self):
        return self.__marks
s = Student()
s.set_marks(90)
print(s.get_marks())
