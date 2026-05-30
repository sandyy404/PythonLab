# Program demonstrating bank account system using inheritance and abstraction
from abc import ABC, abstractmethod
class Bank(ABC):
    @abstractmethod
    def interest(self):
        pass
class SBI(Bank):
    def interest(self):
        print("SBI Interest = 7%")
s = SBI()
s.interest()