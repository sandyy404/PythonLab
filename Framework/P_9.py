# Program to Plot a Pie Chart Using Matplotlib
import matplotlib.pyplot as plt

labels = ['A', 'B', 'C', 'D']
sizes = [30, 25, 20, 25]

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()