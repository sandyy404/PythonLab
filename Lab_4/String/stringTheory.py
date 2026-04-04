# str1 = 'Sandeep'
# str2 = "Sandeep"
# str3 = '''Sandeep'''
# print((str3))
# print((str1))
# print((str2))

# Accessing characters in String.
str1 = "Pandey"
# print(str1[0]) 
# print(str1[1])
# print(str1[2])
# print(str1[3])
# print(str1[4])
# print(str1[5])
# print(str1[6])
# print(str1[7])
# print(str1[-1])
# print(str1[-2])
# print(str1[-3])
# print(str1[-4])
# print(str1[-5])
# print(str1[-6])
# print(str1[-7])
# print(str1[-8])

# String Slicing

str2 = "Pandey"
# print(str2[0:2])    #index 0 to 1
# print(str2[0:])      #index 0 to last
# print(str2[:3])     #index start to 2
# print(str2[::-1])     # start from last to start.

# String Iteration

# str3 = "Kumar"
# for char in str3:
#    print(char, end=" ")

# String Immutability :- Strings are immutable, which means that they cannot be changed.

# str4 = "Hello"
# str4[2] = "34"
# print(str4)

# Deleting a String (it is not possible to delete individual characters from a string).

# s = "How are you?"
# print(s)
# del s
# print(s)  # this will show error. s is not defined

# Updating a String (As strings are immutable, “updates” create new strings using slicing or methods).

# s = "this string will be updated."
# print(s)
# s1 = "T"+s[1:]
# s4 = s[0:12] + "WILL "+ s[17:]
# print(s4)
# print(s1)
# s2 = s.replace("string","Strings")
# print(s2)


# String Methods
# 1:- len()
# str  = "  sandeep kumar pandey  "
# print(len(str))

# 2:- upper() and lower()
# print(str.upper())
# print(str.lower())

# 3:- strip() and replace()   # strip method remove the leading and trailing whitespace from the string
# print(str.strip())
# print(str.replace("pandey","PANDEY"))

#  Concatenating and Repeating Strings

str1 = "Sandeep "
str2 = "Pandey"
# print(str1 + str2)   concatenating
print(str1 *2) #repeating string

# Formatting Strings (Python provides several ways to include variables inside strings.)
# 1:- Using f-strings

# name = "Sandeep"
# age  = 20
# print(f"Name: {name}, Age: {age}")

student = "Ritesh"
sub1M  = 45
sub1  = "Hindi"
sub2M = 48
sub2 = "Math"
sub3M = 40
sub3 = "English"

# print(f"Name:{student}, Subject1: {sub1} {sub1M} , Subject2: {sub2} {sub2M}, Subject3: {sub3} {sub3M} ")

#2:-  Using format()

str = "My name is {} and I am {} years old.".format("Sandeep",21)
print(str)