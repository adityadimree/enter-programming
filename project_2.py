import random

name = input("What is your name ? \n")

print("Good luck !", name)

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
word = random.choice(words)
print("Guess the character.")
guesses = ""
tries = 12 
while tries > 0 :
    failed = 0
    guess = input("Make a guess : ")
    tries-=1
    guesses += guess
    if guess not in word :
        print(f"Wrong ! You have {tries} tries reamaning.")
        if tries == 0 :
            print("You lose ! The word was", word)
    for char in word :
        if char in guesses:
            print(char, end=" \n",)
        else:
            print("_")
            failed+=1
# always remember that loops are the things which happen for once and then for second time and then for third time and then so on...one repitition at a time !
    if failed == 0 :
        print("You win !")
        print("The word is", word)
        quit()