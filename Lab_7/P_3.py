# Program to create an employee class and calculate salary
class Employee:
   def __init__(self,name,basicsalary):
      self.name = name
      self.basicsalary = basicsalary
   def calsalary(self):
       bonus = (20*self.basicsalary)/100
       diwali = (2*self.basicsalary)/100
       totalsal =bonus+diwali+self.basicsalary
       return totalsal 
   
   def salary(self):
      print("The salary of",self.name,"is",self.calsalary())

emp1 =Employee("Pradeep",200000)
# emp1.calsalary()
emp1.salary()  
     