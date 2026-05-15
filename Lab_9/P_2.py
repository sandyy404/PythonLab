#  Program demonstrating multiple inheritance

class Mother:
    mothername = ""
    def mother(self):
        print(self.mothername)
class Father:
    fathername = ""
    def father(self):
        print(self.fathername)
class Son(Mother, Father):
    def parents(self,name):
        self.name = name
        print(self.name,"'s", " Father :", self.fathername)
        print(self.name,"'s", " Mother :", self.mothername)
s1 = Son()
s1.fathername = "RAM"
s1.mothername = "SITA"
s1.parents("Ajay")