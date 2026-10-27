# 1.Write a Python program to create a decorator that logs the arguments and return value of a function.
# 2.Write a Python program to create a decorator to convert the return value of a function to a specified data type.
# 3.Write a Python program to create a decorator function to measure the execution time of a function


#111111111111111111111111

def log_arguments_and_return(func):
    def wrapper(*args, **kwargs):
        # Log the arguments
        print(f"Function '{func.__name__}' called with arguments: {args}, {kwargs}")
        
        # Call the original function
        result = func(*args, **kwargs)
        
        # Log the return value
        print(f"Function '{func.__name__}' returned: {result}")
        
        return result
    return wrapper

# Example usage:
@log_arguments_and_return
def add(a, b):
    return a + b
print(add(3, 5))

