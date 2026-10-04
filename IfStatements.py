# #If Ladder Statements
# marks=int(input("Enter Marks:"))
# if (marks<=100 and marks>=95):
#     print("A+ Grade")
# elif (marks<95 and marks>=90):
#     print("A Grade")
# elif(marks<90 and marks>=85):
#     print("B+ Grade")
# elif(marks<85 and marks>=80):
#     print("B Grade")
# elif(Marks<80 and marks>=75):
#     print("C+ Grade")
# elif(marks<75 and marks>=70):
#     print("C Grade")
# else:
#     print("Fail")


# a=30,b=35,c=43
# if(a>b and b>c):
#     print("A is greater")
# elif(b>c and b>a):
#     print("B is greater")
# else:
#     print("C is greater")

# #Nested if statements
# num=int(input("Enter Number:"))
# if(num>0):  # outer if
#     print("Number is Positive")
#     if(num%2==0):   #inner if
#         print("Number is even")
#     else:
#         print("Number is odd")
# else:
#     print("Number is negative")


#Authentication
username=input("Enter username:")
password=int(input("Enter Password:"))
if(username=="Ashwini" and password==12345):
    print("Login successful")
elif(username=="Ashwini" and password!=12345):
    print("Password is incorrect")
elif(username!="Ashwini" and password==12345):
    print("username is incorrect")
else:
    print("Incorrect")





