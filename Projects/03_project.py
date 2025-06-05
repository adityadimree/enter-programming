from collections import Counter
import random
someWords = '''apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''
someWords = someWords.split() 
word = random.choice(someWords)
chance = len(word)+2
flag = 0
guessed_char = []
for i in word:
  print("_", end=" ")

#take in the input
while chance>0:
    guess = input("Please enter an alphabet : ")
    chance-=1
#guess evaluation gues is a single alphabet
    if len(guess)!= 1:
     print("Enter only a letter !!")
     continue
    if not guess.isalpha():
     print("Enter only a alphabet !!")
     continue
    #adding the guess in the guessed list if it is correct and not if it is not correct
    if guess in guessed_char:
      print("Character already guessed !!")
    elif guess in word:
      guessed_char.append(guess)
      flag+=1
    else:
      print("Wrong guess go for another try !!")

    for i in word:
     if i in guessed_char:
       print(i, end=" ")
     else:
      print("_", end=" ")
    if flag == len(word):
     print("You won!")
     break
print("Chances exhausted.")
print(f"The word was :- {word}")




  









                

            


    

