# Program demonstrating hierarchical inheritance
class Parent:
   def __init__(self,father):
      self.father = father
   def p(self):
      print("Base name ",self.father)


class Son1(Parent):
   def __init__(self, son1, father):
      self.son1 = son1
      super().__init__(father)
   def s1(self):
      print("Father name is:" ,self.father ,"and child 1 name",self.son1)  


class Son2(Parent):
   def __init__(self, son2,father):
      self.son2 = son2
      super().__init__(father)   
   def s2(self):
      print("Father name is:" ,self.father ,"and child 2 name",self.son2) 


class Son3(Parent):
   def __init__(self, son3,father):
      self.son3 = son3
      super().__init__(father)      
   def s3(self):
      print("Father name is:" ,self.father ,"and child 3 name",self.son3)     

c1 = Son1("Dinesh","Rajesh")
c2 = Son2("Priya","Rajesh")
c3 = Son3("Rajneesh","Rajesh")

c1.s1()
c2.s2()
c3.s3()