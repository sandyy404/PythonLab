# # a built-in data structure used to store an ordered, immutable collection of elements.
# # Heterogeneous,Indexed,Allow Duplicates

# # creating tuple

# tup = ()
# print(tup)

# tup = ('Sandeep', 'Kumar',"Pandey")
# print(tup)

# li = [1, 2, 4, 5, 6]
# print(tuple(li))

# tup = tuple('Sandeep')
# print(tup)

# tup = (5, 'Welcome', 7.5, True, [1, 2, 3], {'key': 'value'})
# print(tup)

# # Tuples operations
# tup = tuple("Sandeep")
# print(tup[0])
# print(tup[1:4])  
# print(tup[:3])


# tup = ("Sandeep", "Kumar", "Pandey")

# a, b, c = tup
# print(a)
# print(b)
# print(c)

# # Concatanation of tuple
# tup1 = (0, 1, 2, 3)
# tup2 = ('Sandeep', 'is', 'free')
# tup3 = tup1 + tup2
# print(tup3)

# Slicing of tuple
# tup = tuple("Sandeep")
# print(tup[1:])
# print(tup[::-1])
# print(tup[4:9])

# Deleting a Tuple
tup = (0, 1, 2, 3, 4)
del tup
print(tup)

