# def my_decorator(func):
#     def wrapper():
#         print("Before function execution.")
#         func()
#         print("After function execution.")
#     return wrapper

# @my_decorator  # Using the decorator
# def say_hello():
#     print("Hello, World!")

# say_hello()








# def dec(function):
#     def result():
#         print("executes first")
#         function()
#         print("executes second")
#     return result

# @dec
# def example():
#     print("hi")
# example()



def gen():
    yield 1
    yield 2
    yield 3

g=gen()
print(next(g))