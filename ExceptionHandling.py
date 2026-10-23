#without- try and except
# print("smt-1")
# print(10/0)
# print("smt-3")

# #with try and except block
# print("stmt-1")
# try:
#     print(10/0)
# except ZeroDivisionError:
#     print(10/2)
# print("successfully run")

# try:
#     a=int(input("Enter a number: "))
#     b=int(input("Enter a number: "))
#     c=a/b
#     print(c)
# except ZeroDivisionError:
#     print("Cannot devideed by Zero")
# except ValueError:
#     print("write the value in correct format")


# try:
#     x=int(input("Enter a number: "))
#     y=int(input("Enter a number: "))
#     z=x/y
#     print(z)
# except ArithmeticError:  #this is parent of zero divison error so first we provide this and after zro dvision beacuse python works top to bottom
#     print("Arithmatic error")
# except ZeroDivisionError:
#     print("Cannot divided by Zero")


#Finally block- it also exectes if their is no except block in execute
# try:
#     print("Hello")  #Risky code
#     print(10/5)
# except:
#     print("Handle the situation")
# finally:
#     print("code run sucessfully")


#finally block-it also executes when their is execution of except block
# try:
#     print(10/0)
# except ZeroDivisionError:
#     print("Cannot divided by zero")
# finally:
#     print("code runs")


#finally block- executes when their is no execution of except block and it cannot handle the exception
# try:
#     print(10/0)
# except ValueError:
#     print("cannot divided by zero")
# finally:
#     print("code runss")

#by importing os module's os._exit(0) we cannot executes a finally block
import os
try:
    print("we are in try block")
    os._exit(0)      #immediately terminates the process.0 indicates successful termination.
except:
    print("We are in except block")
finally:
    print("we are in finally block")


