import random
import string
from word import words

def get_word(words):
    word=random.choice(word)
    while '-' in word or ' ' in word:
        word=random.choice(word)

    return word.upper()

def hangman(): 
    word=get_word(word)
    alphabet=set(string.ascii_uppercase).upper()
    used_letters=set()
    # youuuuu leffffttt hereeee
    
    
    
    
user_input=input("Type a something: ")
print(user_input)
    

