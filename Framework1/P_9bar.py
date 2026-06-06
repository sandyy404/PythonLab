import matplotlib.pyplot as plt

students = ["Aman", "Rahul", "Priya"]
marks = [85, 90, 88]

plt.bar(students, marks)

plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()

