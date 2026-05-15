# Program demonstrating multilevel inheritance
class GrandFather:
   def __init__(self,grandfather):
      self.grandfather = grandfather

class Father(GrandFather):
   def __init__(self,father,grandfather):
      self.father =father 
      GrandFather.__init__(self,grandfather)
class child(Father):
   def __init__(self,child,father,grandfather):
      self.child = child
      Father.__init__(self,father,grandfather)
   def generation(self):
      print("GrandFather name:",self.grandfather)
      print("Father'name:",self.father)
      print("Child's name:",self.child) 

s1 = child("Vinod","Dinesh","Prakash")
s1.generation()