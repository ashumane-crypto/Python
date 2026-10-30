# for= iteration(When we know the fix iteration)
for i in range(1,6,2):      # 3 ways to write a for loop (5),(1,6),(1,11,2)
    print(i)

Name="Ashwini"
for i in Name:
    print(i)

#1) 1 to 10 sqaure number
for i in range(1,11):
    print(i*i)

#2)1 to 10 cube number
for i in range(1,11):
    print(i*i*i)

# 3) 1 to 10 even number
for i in range(1,11):
    if(i%2==0):
        print(i)

# 4) 1 to 10 odd number
for i in range(1,11):
    if(i%2!=0):
        print(i)

# 5)Sum of n natural number
num=int(input("Enter A Number "))
sum=0
for i in range(1,num+1):
    sum=sum+i
print("Sum is:",sum)

# 6)Even and their Sum
num=int(input("Enter A Number "))
sum=0
for i in range(1,num+1):
    if(i%2==0):
        sum=sum+i
print("The sum of even number is:",sum)

#7)Odd number and their sum
num=int(input("Enter a number "))
sum=0
for i in range(1,num+1):
    if(i%2!=0):
        sum=sum+i
print("Sum of odd number is :",sum)

#8)Table for n particular number
num=int(input("Enter a number "))
for i in range(1,11):
    print(num,"*",i,"=",num*i)


# 9) Build a Number Pyramid
rows = 5

# Outer loop controls rows
for i in range(1, rows + 1):
    # Inner loop controls columns in each row
    for j in range(1, i + 1):
        print(j, end=" ")
    print()  # Moves to the next line after finishing a row

# Output:
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5


# 10)FizzBuzz Challenge
# Loop from 1 to 15
for i in range(1, 16):
    # Check both first! If a number is divisible by 15, it's divisible by 3 and 5.
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)



# The Modifying-While-Iterating Trap

my_list = [10, 20, 30, 40]
for num in my_list:
    if num == 20:
        my_list.remove(num)
print(my_list)


#Leaking Loop Variables (Scope Leakage)
for x in range(5):
    pass

print("Value of x outside loop:", x)


#The for...else Misconception
def check_numbers(nums):
    for n in nums:
        if n % 2 == 0:
            print("Found an even number:", n)
            break
    else:
        print("No even numbers found.")

print("Test 1:")
check_numbers([1, 3, 5])

print("\nTest 2:")
check_numbers([1, 2, 5])


#Modifying the Iterator Variable Inside the Loop
for i in range(5):
    print(i, end=" ")
    if i == 2:
        i = 4  # Attempting to force the loop to skip to the end








