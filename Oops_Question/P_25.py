# Program demonstrating Hotel Booking System using Encapsulation and Abstraction.
from abc import ABC, abstractmethod
class Hotel(ABC):
    @abstractmethod
    def booking_details(self):
        pass
class Room(Hotel):
    def __init__(self, customer_name, room_no, days):
        self.__customer_name = customer_name
        self.__room_no = room_no
        self.__days = days
        self.__price_per_day = 2000
    def calculate_bill(self):
        total = self.__days * self.__price_per_day
        return total
    def booking_details(self):
        print("Customer Name :", self.__customer_name)
        print("Room Number :", self.__room_no)
        print("Days :", self.__days)
        print("Total Bill :", self.calculate_bill())
r1 = Room("Rohit", 101, 3)
r1.booking_details()