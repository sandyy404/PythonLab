# . Program to create a student class and display details.
class Student:
   def __init__(self,name,age,mark):
      self.name = name
      self.age = age
      self.mark = mark
   def details(self):
      print("Name:-",self.name)
      print("Age:-",self.age)
      print("Mark:-",self.mark)

s1 = Student("Sandeep",20,98)
s1.details()
         