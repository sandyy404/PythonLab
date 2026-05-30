# Program demonstrating Library Management System using Encapsulation and Abstraction.
from abc import ABC, abstractmethod
class Library(ABC):
    @abstractmethod
    def display(self):
        pass
class Book(Library):
    def __init__(self, book_name, author):
        self.__book_name = book_name
        self.__author = author
        self.__issued = False

    def issue_book(self):
        if not self.__issued:
            self.__issued = True
            print("Book Issued Successfully")
        else:
            print("Book already issued")
    def return_book(self):
        self.__issued = False
        print("Book Returned Successfully")
    def display(self):
        print("Book Name :", self.__book_name)
        print("Author :", self.__author)
        print("Issued Status :", self.__issued)
b1 = Book("Python Programming", "Rahul Sharma")
b1.display()
b1.issue_book()
b1.display()
b1.return_book()