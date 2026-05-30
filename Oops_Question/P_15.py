# Program demonstrating polymorphism using method overriding
class Bird:
    def fly(self):
        print("Bird can fly")
class Penguin(Bird):
    def fly(self):
        print("Penguin cannot fly")
p = Penguin()
p.fly()