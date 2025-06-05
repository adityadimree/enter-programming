#Fruit ripeness checker
Fruit = input("Which fruit do you have ? : ")

if Fruit == "Banana" : 
    Colour = input("Please describe the colour of your banana by the options given below:\n1.Green\n2.Yellow\n3.Brown\nInput: ")

    if Colour == "Green" : 
        print("Your fruit is unripe.")
    elif Colour == "Yellow" :
        print("Your fruit is ripe.")
    elif Colour == "Brown" :
        print("Your fruit is overripe.")
    else : 
        print("Please veerify the colour of your Banana.")
else: 
    print("Sorry this program can only tell you the ripeness of a Banana. Also, Bananas are tastier than any other fruit.")
    quit()
 