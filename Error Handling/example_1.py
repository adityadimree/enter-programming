try:
    x = int("Str")#since conversion is not possible this will generate a value error
    inv = 1/x
except ValueError:
    print("Exception is occuring in the 2 line.")
except ZeroDivisionError:
    print("Cannot divide by zero... exception is happening at 3rd line.") 