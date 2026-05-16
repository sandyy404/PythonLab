# Program to find greatest of three numbers using function
def greatest(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c


x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

print("Greatest number is:", greatest(x, y, z))