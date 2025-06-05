import random
import time



def main():
    print("Welcome to the number guessing game, select any two positive integers, a and b and i will select a number betweent them and then you will guess it !!")
    a = int(input("Please provide a(It should be greater than zero) : "))
    b = int(input("Please provide b(It should be greater than a) : "))
    print("Ok, Let me see...")
    time.sleep(3)
    magic_number = random.randint(a, b)
    print("Did it !!!")
    tries = 0
    while tries < 5:
        guess = int(input("Now make a guess, : "))
        tries += 1

        if guess == magic_number :
            print("You got it right !!. Wanna go for another round ?")
            reply = input("Reply (in yes or no): ")
            reply.lower
            if reply == "yes" :
                main()
            else:
                quit("Bye, Nice game.")
        else:
            if tries != 5 :
                print("Tough luck. Make another guess. Tries remaining : ", 5-tries)
            elif tries == 5 :
                print("Maximumm try limit reached !!")
                break
    print("I winn !! the number was", magic_number)
    print("Want to play another round ??")
    reply_2 = input("Reply(Type in yes or no) : ")
    reply_2.lower
    if reply_2 == "yes":
        print("OK")
        main()
    else: 
        quit("Nice game.")
    

        

        
if __name__ == "__main__":
    main()