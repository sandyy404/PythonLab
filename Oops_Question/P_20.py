# Program demonstrating student result system using encapsulation and inheritance
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks
    def result(self):
        if self.__marks >= 40:
            print("Pass")
        else:
            print("Fail")
s = Student("Ravi", 75)
s.result()