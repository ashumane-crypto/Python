# import test
# name=input("Enter your name:")
# test.display(name)

# a=test.person_info["age"]  #dictionary so we use []
# print(a)

# from calculation import *
# a=int(input("Enter a number: "))
# b=int(input("Enter a number: "))

# print(addition(a,b))
# print(substraction(a,b))
# print(mutiplication(a,b))

import calculation as cal  #rename
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))

print(cal.addition(a,b))
print(cal.substraction(a,b))
print(cal.mutiplication(a,b))
