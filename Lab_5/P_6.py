# Program to remove duplicate elements from a list.
# Method:-1
a = [10,20,30,20,15,28,20]
print(list(set(a)))

# Method:-2

b = []
for n in a:
   if n not in b:
      b.append(n)

print("After removing duplicate element:-",b)
