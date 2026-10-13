#Function is reusable block of code
#adv-Reusability,code optimization,time saving process
#UDF-user defined function

def display(): #Function defination
    print("Hello World") #function body
display()
print("Hello Jii HOw are Youu")  #function calling
display()
display()
print("Hiii")

#Non Parameterized/default function
def greet():
    print("Heyy!!")
greet()

#Paramerized FUnction 
def add(a,b):  #Parameter
    print(a+b)
add(20,30)  #Arguments
add(100,200)

# #Reverse program in function
# num=int(input("Enter a number "))    
# def reverse(n):
#     rev=0          #global num  # Tell Python to use the 'num' from outside
#     while(n>0): 
#         rem=n%10
#         rev=rev*10+rem
#         n=n//10
#     print("Reverse number is:",rev)
# reverse(num)

# #Armstrong number program by using function
# num=int(input("Enter a Number: "))
# def armstrong(num):
#     sum=0
#     temp=num
#     while(num>0):
#         rem=num%10
#         sum=sum+rem**3
#         num=num//10
#     print("Armstrong Number is: ",sum)
# if (temp==sum):
#     print("Given number is armstrong")
# else:
#     print("given number is not armstrong")
# armstrong(num)



