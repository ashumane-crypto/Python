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

#pass statement it used to future implementation of function
def demo():
    pass #strore place for future code
demo()

#Types of  argument function in python
#1) Default Argument
def avg(a=5,b=7):
    print("Average is",(a+b)/2)
avg()  #it gives a by default argument from the given parameter

#2) Required argument
def name(fname,lname="Mane"):
    print("My name is :",fname,lname)
name("Ashwini")  #if we did not pass the parametr value then we have to pass the argument in function calling

#3) Keyword Argument
def name(fname,mname,lname):
    print("My name is ",fname,mname,lname)
name(mname="Dhanaji",fname="Ashwini",lname="Mane") #Withoout maintaining order we can call the keyword and value and pass the argument

#4)Variable length function:
    #A)Arbitary function  #Passes many values in argument by tuple
def avg(*average):
    sum=0
    for i in average:
        sum=sum+i
    print("Average of given nmber is:",sum/len(average))
avg(2,3,4,5,7)

    


