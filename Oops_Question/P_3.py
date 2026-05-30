# Hospital Management System using Inheritance
class Hospital:
    def __init__(self, hospital_name):
        self.hospital_name = hospital_name
class Doctor(Hospital):
    def __init__(self, hospital_name, doctor_name, department):
        super().__init__(hospital_name)
        self.doctor_name = doctor_name
        self.department = department
    def display1(self):
        print(f"Hospital       : {self.hospital_name}")
        print(f"Doctor Name    : {self.doctor_name}")
        print(f"Department : {self.department}")
class Patient(Hospital):
    def __init__(self, hospital_name,department,patient_name):
        super().__init__(hospital_name)
        self.department = department
        self.patient_name = patient_name
    def display2(self):
           print(f"Hospital       : {self.hospital_name}")
           print(f"Patient Name       : {self.patient_name}")
d = Doctor("City Hospital", "Dr. Sharma", "Cardiologist")
p1 = Patient("Apollo","Yaad nhi","Sandeep")
d.display1()
p1.display2()