# Program demonstrating encapsulation using private variables
class Person:
    def __init__(self):
        self.__salary = 50000
    def show(self):
        print(self.__salary)
p = Person()
p.show()