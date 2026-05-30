# Program demonstrating vehicle management using inheritance and overriding
class Vehicle:
    def show(self):
        print("Vehicle Information")
class Bike(Vehicle):
    def show(self):
        print("Bike Information")
b = Bike()
b.show()