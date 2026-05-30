# Program demonstrating payment system using abstraction, inheritance,and overriding.
from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass
class UPI(Payment):
    def pay(self):
        print("Payment through UPI")
u = UPI()
u.pay()