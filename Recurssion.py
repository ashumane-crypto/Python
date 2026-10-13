#Factorial
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
print("Factorial of given number is: ",fact(4))