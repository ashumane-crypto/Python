#while= condition(When we don't know the fix iteration)

#Ascending order
i=1
while(i<=10):
    print(i)
    i=i+1

#Descending order
i=10
while(i>=1):
    print(i)
    i=i-1

#Reverse a number
num=int(input("Enter a number "))
rev=0
while(num>0):
    rem=num%10
    rev=rev*10+rem
    num=num//10
print("Reverse number is:",rev)
    

# Palindrome Number
num=int(input("Enter a Number "))
temp=num
rev=0
while(num>0):
    rem=num%10
    rev=rev*10+rem
    num=num//10
print("Reverse Number is:", rev)
if(temp==rev):
    print("Given Number is Palindrome")
else:
    print("Given Number is not Palindrome")


#Amstrong Number
num=int(input("Enter a Number "))
sum=0
temp=num
while(num>0):
    rem=num%10
    sum=sum+rem**3
    num=num//10
print ("Sum of Cubes of Digits is:", sum)
if(temp==sum):
    print("Given Number is Amstrong")
else:
    print("Given Number is not Amstrong")

#Addition of digits
num=int(input("Enter a Number "))
sum=0
while(num>0):
    rem=num%10
    sum=sum+rem
    num=num//10
print("Sum is:",sum)

#Multiplication of digits
num=int(input("Enter a Number "))
mul=1
while(num>0):
    rem=num%10
    mul=mul*rem
    num=num//10
print("Multiplication is:",mul)


