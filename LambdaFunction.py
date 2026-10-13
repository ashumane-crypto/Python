#lambda argument : expression
greatest=lambda a,b:a if a>b else b
# greatest(10,20)
print("Greatest number:",greatest(10,20))

#Square of number
x=int(input("Enter a number: "))
square=lambda x:x*x
print("Square of give number is",square(x))

#cube
y=int(input("Enter a Number: "))
cube=lambda y:y**3
print("Cube of given number is",cube(y))

#Positive-Negative Number check
check=lambda z: "Positive number"  if z> 0 else "Negative NUmber"
print(check(-1))


