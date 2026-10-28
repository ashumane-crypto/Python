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



#  Advanced Production Pattern: Generator Pipelines (Data Engineering)
def raw_data_source():
    """Simulates a stream of raw user registrations from a database."""
    users = [
        {"name": "rahul", "age": 24, "role": "developer"},
        {"name": "sneha", "age": 17, "role": "intern"},  # Underage
        {"name": "amit", "age": 29, "role": "manager"},
        {"name": "priya", "age": 31, "role": "lead"}
    ]
    for user in users:
        yield user

def adult_filter(data_stream):
    """Pipeline Stage 1: Filters out users under 18 years old."""
    for user in data_stream:
        if user["age"] >= 18:
            yield user

def capitalize_names(data_stream):
    """Pipeline Stage 2: Formats user names for database storage."""
    for user in data_stream:
        user["name"] = user["name"].capitalize()
        yield user

# --- Executing the Pipeline ---
# 1. Instantiate the source
raw_stream = raw_data_source()

# 2. Pipe source into the filter
filtered_stream = adult_filter(raw_stream)

# 3. Pipe filtered data into the formatter
processed_stream = capitalize_names(filtered_stream)

print("Processed and Filtered Pipeline Output:")
for clean_user in processed_stream:
    print(clean_user)
