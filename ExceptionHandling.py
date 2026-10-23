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


try:
    x=int(input("Enter a number: "))
    y=int(input("Enter a number: "))
    z=x/y
    print(z)
except ArithmeticError:  #this is parent of zero divison error so first we provide this and after zro dvision beacuse python works top to bottom
    print("Arithmatic error")
except ZeroDivisionError:
    print("Cannot divided by Zero")



