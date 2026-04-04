# Program using built-in list methods

# Creating a list
numbers = [10, 20, 30, 40]

# append() 
numbers.append(50)

# insert() 
numbers.insert(2, 25)

# remove()
numbers.remove(20)

# pop()
numbers.pop()

# sort() 
numbers.sort()

# reverse() 
numbers.reverse()

# count() 
count_10 = numbers.count(10)

# index() 
index_30 = numbers.index(30)

# extend()
numbers.extend([60, 70])

# final list
print("Final List:", numbers)
print("Count of 10:", count_10)
print("Index of 30:", index_30)