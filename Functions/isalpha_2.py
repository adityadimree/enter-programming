string = "34 should leave this string"
number = ""
for char in string:
    if not char.isalpha():
        number+=char

print(number)
