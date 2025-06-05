import random
from collections import Counter

someWords = '''apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''

my_list = someWords.split(' ')

magic_word = random.choice(my_list)

tries = len(magic_word)+2

def main():
    for char in magic_word:
        print("_", end=" ")
    while tries>=1:
        try:
            guess = str(input("Enter an alphabet : "))
        except:
            print("Enter only a alphabet !!")
            continue
        if not guess.isalpha():
            print("Enter only a alphabet !")
            continue
        elif 

