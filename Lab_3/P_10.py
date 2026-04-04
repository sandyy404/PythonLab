# Write a program to check whether a number is divisible by 5 and 11.
num = int(input("Enter a number: "))
if num % 5 == 0 and num % 11 == 0:
    print("Divisible by 5 and 11")
else:
    print("Not Divisible by 5 and 11")