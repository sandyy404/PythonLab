# Plot a line graph using Matplotlib to visualize trends in a dataset.

import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [100, 150, 200, 180, 250]

plt.plot(months, sales, marker='o')

plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.grid(True)

plt.show()