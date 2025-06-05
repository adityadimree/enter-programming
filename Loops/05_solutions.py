input_str = str(input("Type anything "))
for char in input_str :
    print(char)
    if input_str.count(char) == 1 :
        print("The required character is", char)
        break
    #break sidhe pure loop ko hi stop kr deta hai.
    else:
        print("This character is repeating.")