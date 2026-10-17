#Factorial
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
print("Factorial of given number is: ",fact(4))


#Countdown
def countdown(n):
    if n<=0:
        print("Blast OFF")
        return
    print(n)
    countdown(n-1)
countdown(3)