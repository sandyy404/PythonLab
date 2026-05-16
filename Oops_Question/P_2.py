# Program to Implement Online Shopping System using Inheritance.
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def show_product(self):
        print(f"Product : {self.name}")
        print(f"Price   : ₹{self.price}")
class Electronics(Product):
    def __init__(self, name, price, brand):
        super().__init__(name, price)
        self.brand = brand
    def display(self):
        self.show_product()
        print(f"Brand   : {self.brand}")        
e = Electronics("Laptop", 65000, "Dell")
e.display()

