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

# 7)Odd number and their sum
num=int(input("Enter a number "))
sum=0
for i in range(1,num+1):
    if(i%2!=0):
        sum=sum+i
print("Sum of odd number is :",sum)

# 8)Table for n particular number
num=int(input("Enter a number "))
for i in range(1,11):
    print(num,"*",i,"=",num*i)








