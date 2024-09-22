import random
import time

print("Welcome to the hangman game. Here I will randomly select a word and then you have to guess what characters are present in the word. For every correct guess i will release the position of the character you guessed.")

print("The word that i will select will belong to this list.")

someWords = '''apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''

my_list = someWords.split(" ")

for i in my_list :
    print(i)

print("Now let me make a guess.")

time.sleep(3)

magic_word = random.choice(my_list)

print("Guessed it !! Hint : It is a fruit's name.")

tries = len(magic_word) + 2

while tries >= 1 :
    guess = input("Make a guess ! : ")
    tries-=1
    meset = set()
    meset2 = set(magic_word)
    if guess in magic_word :
        print("You guessed it right !")
        position = magic_word.index(guess) 
        print(f"Position of the guess in the word is : {position}")
        meset.add(guess)
    if meset == meset2:
        print(f"You have guessed all the letters !! You win.{magic_word} is the word.")
        quit("See you in the next game.")
    else:
        print("Try again ! Tries remaining", tries)
print("I winn!! All tries exhausted. The word was", magic_word)
