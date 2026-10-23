#Armstrong Number Prpgram by calling that in Main1.py module

# def armstrong(num):
#     temp=num
#     sum=0
#     digits=len(str(num))
#     while num>0:
#         rem=num%10
#         sum=sum+rem**digits
#         num=num//10
#     if temp==sum:
#         print(" Armstrong Number")
#     else:
#         print(" Not Armstrong Number")


def palindrome(num):
    temp=num
    rev=0
    while num>0:
        rem=num%10
        rev=rev*10+rem
        num=num//10
    if temp==rev:
        print("palindrome")
    else:
        print("not palindrome")