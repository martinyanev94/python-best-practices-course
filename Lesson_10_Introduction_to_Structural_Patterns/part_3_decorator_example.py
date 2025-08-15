def simple_function():
    return "This is a simple function."

def logger_decorator(func):
    def wrapper():
        print("Function is being called...")
        result = func()
        print("Function call completed.")
        return result
    return wrapper

decorated_function = logger_decorator(simple_function)
print(decorated_function())
