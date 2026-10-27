#decorator-adds extra functionality ,symbol of defining decorator is @
# def decor(func):
#     def inner(name):
#         if name=="Sunny":
#             print("Hello Sunny Bad Morning")
#         else:
#             func(name)
#     return inner

# @decor
# def wish(name):
#     print("Hello",name,"Good Morning")
# wish("Chinny")
# wish("Buuny")
# wish("Sunny")



#without using and decor 
def decor(func):
    def inner(name):
        if name=="Sunny":
            print("Hello Sunny Bad Morning")
        else:
            func(name)
    return inner

def wish(name):
    print("Hello",name,"Good Morning")
decorfunction=decor(wish)  #we store the wish function in decorationfunction variable

wish("Chinny") #decorator not executed
wish("Buuny")
wish("Sunny")

decorfunction("Sunny") #and then passes the value to the decoration function andthe decorator executed
decorfunction("Bunny")


        
    

