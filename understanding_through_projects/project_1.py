import math
import random
upper  = int(input("Enter the upper bound : "))
lower = int(input("Enter the lower bound : "))

chances = math.ceil(math.log(upper-lower+1, 2))

print(f"You have {chances} to guess the correct number.")

flag = False
Magic_number = random.randint(lower, upper)

while chances>0:
    guess = int(input("Make a guess : "))
    chances-=1
    if guess == Magic_number:
        print("Congratulations ! You win.")
        flag = True
        break
    elif guess>Magic_number:
        print("You guessed it too high.")
    elif guess<Magic_number:
        print("You guessed it too low.")
if not flag:
    print("You lose. All chances used up !")
    print(f"The number was {Magic_number}.")