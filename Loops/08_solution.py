number = int(input("Please enter an whole number of your choice : "))
is_prime = True

#jb sir ne prime number ki definition dekhi toh unhone har ek condition ko apne loop me incorporate kiya to tum khu adha adhoora code likho har ek condition ko apply karo.

if number > 1 :
    for i in range(2, number):
        if (number%i) == 0 :
            is_prime = False
            break
      
print(is_prime)
            


