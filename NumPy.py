# import numpy as np  #by alising we can import
# arr=np.array([1,2,3,4,5])
# print(arr)

# import numpy #without alising
# arr=numpy.array([1,2,3,4,5])
# print(arr)

#Types of array
#1) 0D-scalar-()
#2) 1D- vector-[]
# )2D-Matrix-[[]]
#4)Multi-dimenssional-[[[]]]

# import numpy as np
# arr0=np.array(5)  #)0D
# arr1=np.array([1,2,3,4,5])  #1D
# arr2=np.array([[1,2,3],[5,7,9]])  #2D
# arr3=np.array([[12,13],[14,15],[16,17],[18,19]]) #Multidimensional
# print(arr0)
# print(arr1)
# print(arr2)
# print(arr3)

# import numpy as np
# arr=np.array([1,2,3,4])
# print(arr.dtype)  #int64 because for in it take 4 bytes

# arr1=np.array([0.1,0.2,0.3])  
# print(arr1.dtype)

# arr2=np.array(['a','b','c'])
# print(arr2.dtype)

# import numpy as np
# x=np.array([3,5])
# y=np.array([2,5])
# print("Original array")
# print(x)
# print(y)
# print("Comparison")
# print(np.greater(x,y))
# print("Greater that equals")
# print(np.greater_equal(x,y))
# print("comparison less")
# print(np.less(x,y))
# print("Comparison less equals")
# print(np.less_equal(x,y))

# import numpy as np
# a=np.array([1,2,4,11,56,78,90,44,5,3,22,9])
# print(a)
# print("reshape into 4 rows and 3 columns")
# na=a.reshape(4,3)  #rows and columns
# print(na)


# print("Reshaping into 2 array,2 rows and 3 columns")
# naa=a.reshape(2,2,3)  #arrays-rows-columns
# print(naa)


# print("to print given array in 1D")
# for x in a:  #for 1D array
#     print(x)

# import numpy as np
# a=np.array([[1,2],[4,5],[7,4],[9,4]])
# for i in a:
#     print(i)

# for x in np.nditer(a):  #provide an n dimenssinal iteration
#     print(x)

# #search element index
# n=np.where(a==4)
# print(n)  #returns the index of 4


import numpy as np
a=np.array([2,4,6,5,1,2])
n=np.where(a%2==0)  #returns the index of even number
print(n)
print(np.sort(n))


