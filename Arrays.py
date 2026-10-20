# import array as arr
# a=arr.array("i",[2,4,6,8])
# print(a)

# from array import *  #import all modules of array
# a1=arr.array("i",[1,2,3,4,6,8])
# print(a1)

import array as arr
num=arr.array("i",[1,2,3,4,6,8])
num[0]=0 #add element in particular index
print(num)
del num[2]  #deleting particular element from index
print(num)


#concatination 
import array as arr
a=arr.array("d",[0.1,0,4,0.6])
b=arr.array("d",[2.1,3.1])

c=a+b
print(c)


import array as arr
num1=arr.array("i",[1,2,3,4,5])
num1[2:5]=arr.array("i",[4,6,8])
print(num1)



# 1. Adding Elements (append, insert, and extend)

import array as arr

# Initialize an integer array
numbers = arr.array('i', [10, 20, 30])

# 1. append(): Adds an element to the VERY END
numbers.append(40)
print("After append:", numbers)  # Output: array('i', [10, 20, 30, 40])

# 2. insert(): Adds an element at a SPECIFIC INDEX -> insert(index, value)
numbers.insert(1, 15)  # Inserts 15 at index 1
print("After insert:", numbers)  # Output: array('i', [10, 15, 20, 30, 40])

# 3. extend(): Adds multiple elements from another array/iterable to the end
more_numbers = arr.array('i', [50, 60])
numbers.extend(more_numbers)
print("After extend:", numbers)  # Output: array('i', [10, 15, 20, 30, 40, 50, 60])


# 2. Removing Elements (pop and remove)
import array as arr

numbers = arr.array('i', [10, 20, 30, 20, 40])

# 1. pop(): Removes and returns an element by its INDEX (defaults to the last item)
removed_item = numbers.pop(2)  # Removes the element at index 2 (which is 30)
print("Popped item:", removed_item)
print("Array after pop:", numbers)  # Output: array('i', [10, 20, 20, 40])

# 2. remove(): Removes the FIRST occurrence of a specific VALUE
numbers.remove(20)  # Removes the first 20 it finds
print("Array after remove:", numbers)  # Output: array('i', [10, 20, 40])



# 3. Searching and Counting (index and count)
import array as arr

letters = arr.array('u', ['a', 'b', 'c', 'a', 'b', 'a'])  # 'u' is for Unicode characters

# 1. count(): Counts how many times a value appears
a_count = letters.count('a')
print("Number of 'a's:", a_count)  # Output: 3

# 2. index(): Finds the index position of the FIRST occurrence of a value
b_position = letters.index('b')
print("First 'b' is at index:", b_position)  # Output: 1


# 4. Advanced Slicing (Slicing with Steps)
import array as arr

numbers = arr.array('i', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Get every second element (step of 2)
even_indices = numbers[0:10:2]
print("Every 2nd element:", even_indices)  # Output: array('i', [0, 2, 4, 6, 8])

# Reverse an array using a negative step
reversed_array = numbers[::-1]
print("Reversed array:", reversed_array)  # Output: array('i', [9, 8, 7, 6, 5, 4, 3, 2, 1, 0])


# 5. Converting Arrays to Standard Lists
import array as arr

numbers_array = arr.array('i', [5, 10, 15])

# tolist(): Converts the array to a normal Python list
numbers_list = numbers_array.tolist()

print("Type of numbers_array:", type(numbers_array))  # Output: <class 'array.array'>
print("Type of numbers_list:", type(numbers_list))    # Output: <class 'list'>
print("List data:", numbers_list)                      # Output: [5, 10, 15]



