# Program demonstrating Railway Reservation System using Encapsulation and Abstraction.
from abc import ABC, abstractmethod
class Railway(ABC):
    @abstractmethod
    def reservation_details(self):
        pass
class Ticket(Railway):
    def __init__(self, passenger_name, train_name, seat_no):
        self.__passenger_name = passenger_name
        self.__train_name = train_name
        self.__seat_no = seat_no
        self.__status = "Confirmed"
    def cancel_ticket(self):
        self.__status = "Cancelled"
        print("Ticket Cancelled")
    def reservation_details(self):
        print("Passenger Name :", self.__passenger_name)
        print("Train Name :", self.__train_name)
        print("Seat Number :", self.__seat_no)
        print("Status :", self.__status)
t1 = Ticket("Ankit", "Rajdhani Express", "S1-45")
t1.reservation_details()
t1.cancel_ticket()
t1.reservation_details()