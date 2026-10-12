# Tuple is impuutable collections of data
# It is faster that list
# It is similar to list because in tuple we also store different type of data
# Tuple is represented by () paranthesis
# it is read only data type because we only read the data in tuple but cannot change

# convert tuple in list
tuple=(1,2,3,4,4,5)
list=list(tuple)
print(list)
print(tuple)

#Tuple Methods
tuple1=(1,2,2,4,5,7,9,4,3)
print(tuple1.index(2))  #To find index of given value
print(tuple1.count(2))  #Occurence of element

#Tuple Functions

print(len(tuple1)) #to find lenth
print(max(tuple1))   #to find maximum value
print(min(tuple1))  #To find minimum value
print(sum(tuple1))  #To find sum of element
print(sorted(tuple1)) #To sorting list
