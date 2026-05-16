# Program to Implement Person → Employee → Manager using Multilevel Inheritance.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_person(self):
        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")
class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.salary = salary
    def display_employee(self):
        print(f"Employee ID : {self.emp_id}")
        print(f"Salary      : {self.salary}")
class Manager(Employee):
    def __init__(self, name, age, emp_id, salary, department):
        super().__init__(name, age, emp_id, salary)
        self.department = department
    def display_manager(self):
        self.display_person()
        self.display_employee()
        print(f"Department  : {self.department}")
m = Manager("Rahul", 35, "E101", 90000, "IT")
m.display_manager()