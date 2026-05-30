# Program demonstrating shape area calculation using abstraction and overriding
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def area(self):
        l = 5
        b = 4
        print("Area =", l * b)
r = Rectangle()
r.area()