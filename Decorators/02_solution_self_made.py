def decorators(func):
    def wrapper(*args, **kwargs):
        args_value = ", ".join(str(arg) for arg in args)
        kwargs_value = ", ".join(f"{k} = {v}" for k, v in kwargs.items())
        print(f"calling : {func.__name__}, with arguments : {args_value}, and kwargs {kwargs_value}")
        result = func(*args, **kwargs)
        return result
    return wrapper


@decorators
def greetings(name, greeting = "Hello"):
    print(f"{greeting}, {name} !!")

greetings("Chai", greeting="Hanji")