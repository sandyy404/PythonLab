# Program demonstrating ATM Machine System using Data Abstraction
from abc import ABC, abstractmethod
class ATM(ABC):
    @abstractmethod
    def transaction(self):
        pass
class Withdraw(ATM):
    def transaction(self):
        print("Cash Withdrawn")
w = Withdraw()
w.transaction()