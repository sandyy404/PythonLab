# Write a program to print a pyramid or triangle pattern using nested loops
n = 6
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()