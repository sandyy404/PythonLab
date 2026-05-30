# Program demonstrating Electricity Bill Calculation using Data Abstraction.
from abc import ABC, abstractmethod
class ElectricityBill(ABC):
    @abstractmethod
    def calculate_bill(self):
        pass
class HomeBill(ElectricityBill):
    def __init__(self, customer_name, units):
        self.__customer_name = customer_name
        self.__units = units
    def calculate_bill(self):
        if self.__units <= 100:
            bill = self.__units * 5
        elif self.__units <= 200:
            bill = self.__units * 7
        else:
            bill = self.__units * 10
        return bill
    def display(self):
        print("Customer Name :", self.__customer_name)
        print("Units Consumed :", self.__units)
        print("Total Bill :", self.calculate_bill())
c1 = HomeBill("Sandeep", 250)
c1.display()