while True :
#ye while true likh ke tumne bas whle loop ko incorporate kiya hai apne programm me. Us loop ko chalane ke ek zariya hai ye syntax.
    number = int(input("Please enter a number between 1 and 10: "))
    #input method se jo bhi ata hai vo strings me ata hai isliye uske datatype ko badalke integer me karna bahut zaroori. 
    if 1<=number<=10 :
        print("Thanks !")
        break
    else :
        print("Try again.") 