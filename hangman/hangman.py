import random
import string
from words import words

def get_word(words):
    word=random.choice(word)
    while '-' in word or ' ' in word:
        word=random.choice(word)

    return word.upper()

def hangman(): 
    word=get_word(word) #letters in the word
    word_letters=set(word)
    alphabet=set(string.ascii_uppercase).upper()
    used_letters=set() #alredy gussed letter by the user
    # youuuuu leffffttt hereeee
    
    #getting the input
    while len(word_letters)>0:
        #ued letters 
        print('You have alredy used these letters: ',' '.join(used_letters))
        word_list= [letter if letter in used_letters else '-' for letter in word]
        print('current word: ', ' '.join(word_list))
        user_letter=input('Guess a letter: ').upper
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        
        elif user_letter in used_letters:
            print("alredy gussed, try again")
        
        else:
            print("invalid char. Try again.")
    
    
    
    


    

