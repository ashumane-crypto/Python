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


#sum of list program by recursion
def sum_with_loop(number):
    total=0
    for num in number:
        total=total+num
    return total
print("Total sum of list is",sum_with_loop([2,3,4,5,]))

    