# Allows duplicate elements,Mutable,Ordered,Index-based

# Creating a List
# 1. Using Square Brackets

a = [1, 2, 3, 4, 5] 
b = ['apple', 'banana', 'cherry'] 
c = [1, 'hello', 3.14, True]
print(a)
print(b)
print(c)

# 2. Using list() Constructor

d = list((1, 2, 3, 'apple', 4.5))  
print(d)
e = list("GFG")
print(e)

# 3. Creating List with Repeated Elements

f = [2] * 5
g = [0] * 7

print(f)
print(g)

# Accesing the elements

A = [10,20,30,40,50]
print(A[0])    
print(A[-1])
print(A[1:4])

# Adding the elements into list
# M:-1 append()
# M:-2 extend()
# M:-3 insert()
A.append(60)  
print("After append(50):", A)

A.extend([18,20,30])
print("After extend([15, 20, 25]):", A)

A.insert(0,5)
print("After insert(0, 5):", A)

# All clear the elements of the list
f.clear()
print("After clear():", f)

# Updating elements into list

A[1] = 12
print("After updating at index 1",A)

# Removing the elements fron list
# remove()

A.remove(25)
print("After remove(25):", A)

# pop()

popped = A.pop(3)
print("Popped element:", popped)
print("After pop(1):", A)

# del

del A[5]  
print("After del a[0]:", A)


# Iterating over list
for item in g:
   print(item)

   