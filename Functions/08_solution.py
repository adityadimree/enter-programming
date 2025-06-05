#Aim - create a function that accepts any number of keyword arguments  and prints them in the format - key: value.
#what are keyword arguments ? Key : key ki value -- together they make keyword argument.
#*args keyword se multiple arguments tuple ki tarah treat ho jate the, and hum unpe loop laga lete the.. yaha pe use hota hai **kwargs

def print_kwargs(**kwargs):
    print(kwargs)
    for a, b in kwargs.items():
        print(f"{a}: {b}")




print_kwargs(name = "Shaktiman", power = "Lazer")
print(print_kwargs(name = "shaktiman", power = "Lazers", villian = "Dr. Jackal"))
print(print_kwargs(name = "shaktiman",))
