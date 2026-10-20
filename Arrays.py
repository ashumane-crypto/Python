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


# import array as arr
# num1=arr.array("i",[1,2,3,4,5])
# num1[2:5]=arr.array("i"[4,6,8])
# print(num1)

