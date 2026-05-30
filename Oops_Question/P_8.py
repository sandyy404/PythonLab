# Program demonstrating method overloading using default arguments
class Addition:
    def add(self, a, b=0, c=0):
        print("Sum =", a + b + c)

obj = Addition()
obj.add(5)
obj.add(5, 10)
obj.add(5, 10, 15)