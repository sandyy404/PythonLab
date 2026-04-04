# Write a program to calculate the sum of digits of a given number using a loop.
num = 65
sum_digits = 0
while num > 0:
    digit = num % 10
    sum_digits += digit
    num //= 10
print("Sum of digits =", sum_digits)
