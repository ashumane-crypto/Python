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

#List Operation

list1=[1,2,3]
list2=[4,9,7]

print(list1 + list2)  #Concatination- mrge
print(list1 * 4)  #Repetition-how many time you want to repeat the list

#List Methods

#Adding Elements
fruits=["Apple","Orange","Kiwi","Mango","Banana",1,2,2]

fruits.append("Watermalon")  #1)Append-append adds element at the end
print(fruits)
fruits.extend([3,5]) #2)Extend- to add list in the existing list
print (fruits)
fruits.insert(2,"Lemon") #3)Insert-to insert item at specific index(index,value)
print(fruits)

#Removing Element
fruits .pop()  #1) Removes the lat element
print(fruits)

fruits.remove(3) #2)give direct value to which you have to remove
print(fruits)

# fruits.clear() #3)To remove all the elements from list
# print(fruits)

#Finding and Information
print(fruits.index("Lemon")) #1)To find index of value

print(fruits.count(2)) #2)To count how many numbers are particular element is appear

#Ordering and copyig
num=[1,4,9,3,0]
num.sort()  #1)It only works for sorting the list in form of integer
print(num)
print(sorted(num))
fruits.reverse() #2)it reverse the list work for all
print(fruits)
newNum=num.copy() #3)Returns the shallow copy of the list
print(newNum)






