# Program demonstrating Hospital Patient Record System using Encapsulation and Abstraction.
from abc import ABC, abstractmethod

class Hospital(ABC):
    @abstractmethod
    def patient_details(self):
        pass
class Patient(Hospital):
    def __init__(self, name, age, disease):
        self.__name = name
        self.__age = age
        self.__disease = disease
    def update_disease(self, new_disease):
        self.__disease = new_disease
        print("Disease Updated")
    def patient_details(self):
        print("Patient Name :", self.__name)
        print("Age :", self.__age)
        print("Disease :", self.__disease)
p1 = Patient("Aman", 22, "Fever")
p1.patient_details()
p1.update_disease("Typhoid")
p1.patient_details()