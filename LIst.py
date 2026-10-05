# List- store diffferent data types in them  and it is mutable
# In list indexing start from 0 (Forward to Backward,+ve indexing)
# in LIst indexing start from -1 (Backward to Forward,-ve indexing)
# List is mutable and it is denoted by []

l=[10,20.5,"Ashwini",True,20.5]
print(l)
print(type(l))
print(len(l))
print(id(l))

#indexing- we can access only one element by indexing
print(l[3])
print(l[-4])


#Nested List- we can store list inside list
l1=[10,20.5,"Ashwini",[10,20,30],["Virat", "Rohit"],True,20.5]
print(l1)

print(l1[3])
print(l1[3][1])
print(l1[4][0][0])
print(l1[4][1][0])

#Slicing- we can access multiple elements by slicing

a=[10,20,30,40,50,60]
print(a[1:4:2])  #Start:Stop:Step 
print(a[::2])
print(a[::1])

#Reverse the list
b=[1,20,40,50,56]
print(b[::-1])


