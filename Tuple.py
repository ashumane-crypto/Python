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


# Tuple Unpacking & Variable Swapping
# 1. Tuple Unpacking
person = ("Amit", 25, "Software Engineer")
name, age, profession = person

print(f"{name} is a {age}-year-old {profession}.")
# Output: Amit is a 25-year-old Software Engineer.

# 2. The Swap Trick
a = 10
b = 99
print(f"Before swap: a={a}, b={b}")

# Python implicitly creates a tuple here to swap the references
a, b = b, a

print(f"After swap: a={a}, b={b}")
# Output: After swap: a=99, b=10


# Basic Tuple Slicing and Reversal
alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')

# Get elements from index 2 to 5 (exclusive)
middle_part = alphabet[2:5]
print("Sliced segment:", middle_part) 
# Output: ('c', 'd', 'e')

# Reverse the tuple using a step of -1
reversed_alphabet = alphabet[::-1]
print("Reversed tuple:", reversed_alphabet)
# Output: ('h', 'g', 'f', 'e', 'd', 'c', 'b', 'a')




