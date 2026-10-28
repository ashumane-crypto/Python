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


# #noramal function return 10 and then stop
# def normal():
#     return 10
#     return 20

# #with generator yield 10 pauses the function. When another value is requested, it continues and can produce 20.
# def generator():
#     yield 10
#     yield 20

# Custom Sequence Generator
def count_up_to(maximum):
    """A simple generator that counts from 1 up to a maximum number."""
    count = 1
    while count <= maximum:
        yield count  # The function pauses here, returns the value, and resumes on the next call
        count += 1

# Consuming the generator
counter = count_up_to(3)

print("First call:", next(counter))
print("Second call:", next(counter))
print("Third call:", next(counter))

# Calling next() again would raise a StopIteration error. 
# Instead, we typically loop over them cleanly:
print("\nLooping through a new generator instance:")
for number in count_up_to(5):
    print(number)
