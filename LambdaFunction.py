#A lambda function in Python is simply a shortcut to create a quick, 
# one-line function without giving it a formal name.
#it is also called as anonymous (nameless)
#adv--Saves Space (Less Code):,No Need to Invent Names.

#lambda argument : expression
greatest=lambda a,b:a if a>b else b
# greatest(10,20)
print("Greatest number:",greatest(10,20))

#Square of number
x=int(input("Enter a number to find square: "))
square=lambda x:x*x
print("Square of give number is",square(x))

#cube
y=int(input("Enter a Number to find cube: "))
cube=lambda y:y**3
print("Cube of given number is",cube(y))

#Positive-Negative Number check
check=lambda z: "Positive number"  if z> 0 else "Negative NUmber"
print(check(-1))

#Even-odd
Even_Odd=lambda a: "Even" if a%2==0 else "Odd"
print("The given number is :",Even_Odd(4))

#Vote Management
vote=lambda b:"Eligible for vote" if b>=18 else "You are not eligible for vote"
print(vote(19))


# Marks 
marks=lambda c:"Pass" if c>35 else "Fail"
print("You are",marks(80),"in exam")

#Map-It executes a function for each item in an iterable (list, tuple etc.) and returns a list of the results.
def sq(x):
    return x*x
t=(9,2,3,4,5,6,7)
ut=(map(sq,t))
print(list(ut))



