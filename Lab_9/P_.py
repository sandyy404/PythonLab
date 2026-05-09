# Program demonstrating single inheritance
class Animal:
   def __init__(self,name):
      self.name =name
   def info(self):
      print("Animal's name:-",self.name)
class Dog(Animal):
   def sound(self):
      print(self.name,"barks")
dog = Dog("Piyush")      
dog.info()
dog.sound()