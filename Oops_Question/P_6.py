# Mobile Phone Feature Extension using Inheritance.
class Mobile:
    def call(self):
        print("Calling feature available")
class SmartPhone(Mobile):
    def internet(self):
        print("Internet feature available")
sp = SmartPhone()
sp.call()
sp.internet()