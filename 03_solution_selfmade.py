import time
def cache(func):
    def wrapper(*args):
        chache_value = {}
        print(chache_value)
        if args in chache_value:
            return chache_value[args]
        result = func(*args)
        return result
    return wrapper




@cache
def long_running_function(a, b):
    time.sleep(4)
    return a + b
print(long_running_function(6, 7))
print(long_running_function(6, 7))