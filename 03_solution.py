number = int(input("Please enter an positive integer of your choice : "))

for variable in range(1, 11) :
    #variable ki kisi specific value ke liye loop nhi chalana chahte ?? you can use the continue keyword. Ye kisi ek specific turn ko stop kr deta hai.
    if variable == 5:
        continue
    print(number, "x", variable, "=", number*variable)