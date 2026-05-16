# Library Management System using Inheritance
class LibraryItem:
   def __init__(self,types):
       self.types = types
   def type(self):
       print("The type of the book is ",self.types)

class Books(LibraryItem):
    def __init__(self, types,name,author):
        super().__init__(types)
        self.author = author
        self.name = name
    def bookdetails(self):
        print("Type of of the book ",self.types)
        print("Author of the book is ", self.author)  

i = LibraryItem("Social Fiction")
i.type()
book1 =Books("Godaan","Social Fiction","Munshi Premchand") 
book2 = Books("Gunahon Ka Devta","Romantic Fiction","Dharamvir Bharati")
book1.bookdetails()
book2.bookdetails()

