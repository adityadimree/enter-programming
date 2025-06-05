#Fail. You did not undrestood the prject requirement carefully.
import random
import time

name = input("What is your name ? : ")

print(f"{name}, welcome to the word guessing game ! I have a list of words as shown.")

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
for variable in words :
    print(variable)

print("Now i will select any one of these words without telling you. You will guess an alphabet, if the guessed alphabet is part of the randomly selected word you win!. You can only make 12 guesses.")
time.sleep(10)
random_word = random.choice(words)
print("Okay ! I selected the word.")
tries = 12
while tries >= 1 :
    guess = input("Make your guess. : ")
    tries -= 1
    if guess in random_word :
        print("Nice luck ! You win. The word was ",random_word )
        quit("See you !")
    else:
        print(f"Tough luck ! {tries} tries reamaining.")
print("I win ! You used all your tries. The word was ",random_word)
quit("See you next time !")


