#  Program to find largest and smallest element in a list

a = [10,25,2,63,85,567]
lar = a[0]
small = a[0]
for i in a:
   if(lar<i):
      lar = i 
   if(small>i):
      small = i   
print("Largest element:-",lar)    
print("Smallest element:-",small)  
