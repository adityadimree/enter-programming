#definig a function which helps the computer to calculate the numbers
def comp_chance(num):
    if(num>=4):
        nearest_multiple = num + (4-(num%4))#i do not know why but this algorithm works for numbers greater than 4 for any other case it will just give 8
    else:
        nearest_multiple=4
    return nearest_multiple
def lose1():
    print("\n\nYOU LOSE !")
    print("Better luck next time !")
    exit(0)
#checks whether the numbers are consecutive
def check(xyz):
    i=1
    while i<len(xyz):
        if(xyz[i]-xyz[i-1]) != 1:
            return False
        i = i+1
    return True

def start1():
    xyz=[]
    last = 0
    while True:
        print("Enter 'F' to take the first chance.")
        print("Enter 's' to take the second chance.")
        chance = input('> ')

        # player takes the first chance
        if chance == "F" :
            while True:
                if last == 20:
                    lose1()
                else:
                    print("\nYour Turn.")
                    print("\nHow many numbers do you wish to enter ?")
                    inp = int(input('> '))

                    if inp>0 and inp<=3:
                        comp = 4-inp
                    else:
                        print("Wrong input. You are disqualified from the game.")
                        lose1()
                    i, j = 1, 1
                    print("Now enter the values")
                    while i <=inp:
                        a = input("> ")
                        a = int(a)
                        xyz.append(a)
                        i+=1

                    #stores the last element of xyz
                    last=xyz[-1]    

                    #checking if the input is consecutive 
                    if check(xyz) == True:
                        if last == 21:
                            lose1()
                        else:
                            #computer's turn
                            while j <= comp:
                                xyz.append(last+j)
                                j=j+1
                            print("Order of inputs after computer's turn is: ")
                    else:
                        print("\nYou did not input consecutive integers.")
                        lose1()

        #player takes the second chance 
        elif chance == "S":
            comp = 1
            last = 0
            while last<20:
                #computer's turn
                j=1
                while j<=comp:
                    xyz.append(last + j)
                    j = j+ 1
                print ("Order of inputs after computer's turn is:")
                print(xyz)
                if xyz[-1] == 20:
                    lose1()
                else:
                    print("\nYour turn.")
                    print("\n How many numbers would like to add ?")
                    inp = int(input("> "))
                    i=1
                    while i<=inp:
                        xyz.append(int(input('> ')))
                        i+=1
                    last = xyz[-1]
                    if check(xyz) == True:
                        near= comp_chance(last)
                        comp = near - last
                        if comp == 4:
                            comp = 3
                        else:
                            comp = comp
                    else:
                        print("\nYou did not enter consecutive integers.")
                        lose1()
            print("\n\nCONGRATULATIONS !!!")
            print("YOuo won !")
            exit(0)
        else:
            print("wrong choice") 

game = True
while game== True:
    print("Player 2 is computer.")
    print("Do you want to play the 21 number game ?(Yes / NO)")
    ans = input("> ")
    if ans == 'Yes':
        start1()
    else:
        
        print ("Do you want quit the game?(yes / no)")
        nex = input('> ')
        if nex == "yes":
                print ("You are quitting the game...")
                exit(0)
        elif nex == "no":
                print ("Continuing...")
        else:
                print ("Wrong choice")                    


