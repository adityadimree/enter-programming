import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, *kwargs)
        end  = time.time()
        print(f"The function {func.__name__} ran in {end-start} seconds.")
        return result
    return wrapper
@timer
def stopper(n):
    time.sleep(n)

stopper(2)
