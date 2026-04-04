# Write a program to reverse a given number using a loop.
num = 45
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
print("Reversed number:", reverse)