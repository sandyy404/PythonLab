#  Program to check palindrome using function
def palindrome(n):
    original = n
    reverse = 0

    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10

    if original == reverse:
        return True
    else:
        return False


num = int(input("Enter a number: "))

if palindrome(num):
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")