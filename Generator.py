# def get():
#     for i in range(1,10001):
#         yield i
# data=get()
# print(next(data))
# print(next(data))
# print(next(data))

# def demo():
#     print("start")
#     yield 10
#     print("middle")
#     yield 30
#     print("end")
#     yield 50
# g=demo()
# print(next(g))
# print(next(g))
# print(next(g))


#noramal function return 10 and then stop
def normal():
    return 10
    return 20

#with generator yield 10 pauses the function. When another value is requested, it continues and can produce 20.
def generator():
    yield 10
    yield 20

