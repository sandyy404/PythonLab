# Program to Plot a Bar Chart Using Matplotlib
import matplotlib.pyplot as plt

subjects = ['Math', 'Science', 'English']
marks = [85, 90, 75]

plt.bar(subjects, marks)
plt.title("Bar Chart")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()