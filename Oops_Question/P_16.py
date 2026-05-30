# Program demonstrating employee management using inheritance and encapsulation
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
    def display(self):
        print(self.name, self.__salary)
class Manager(Employee):
    pass
m = Manager("Amit", 70000)
m.display()