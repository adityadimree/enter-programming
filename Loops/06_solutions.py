number = int(input("Enter any positive integer of your choice : "))
starting = 1
while number > 0 :#while loop ki yahi khaasiyat hai ise ek true for false ki condition dedo or jb jb the given cocndition is satisfied the loop is runned and if the condition is not fullfilled the loop does not runs.
    #starting = starting * number
    #number = number - 1
    starting*=number
    number-=1
    
print("the required factorial is :", starting)