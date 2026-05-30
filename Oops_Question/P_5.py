# College Management System using Inheritance.
class College:
    def __init__(self, college_name):
        self.college_name = college_name
class Student(College):
    def __init__(self, college_name, student_name, roll_no):
        super().__init__(college_name)
        self.student_name = student_name
        self.roll_no = roll_no
    def display(self):
        print(f"College : {self.college_name}")
        print(f"Student : {self.student_name}")
        print(f"Roll No : {self.roll_no}")
s = Student("Galgotias University", "Sandeep","24SCSE1010485" )
s.display()