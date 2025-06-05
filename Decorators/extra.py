def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"calling function : {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function : {func.__name__} finished execution.")
        return result
    return wrapper
@my_decorator
def say_hello(name):
    return f"Hello {name}"

print(say_hello("Aditya"))