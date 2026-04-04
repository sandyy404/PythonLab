# Write a program to check whether a character is a vowel or consonant.
ch = input("Enter a character: ")
if ch.lower() in "aeiou":
    print("Vowel")
else:
    print("Consonant")