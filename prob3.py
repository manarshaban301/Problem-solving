#manar shaban moubarak

import random

def word_scrambled_game():
    words=["red","blue","green","yellow","pink"]
    
    chosen_word = random.choice(words)
    
    scrambled_word = ''.join(random.sample(chosen_word, len(chosen_word)))

    print("welcome to the word scrambled game!!")
    print(f"try to guess the word from its scrambled version:{scrambled_word}")
    print("you have only 5 attempts to go.")

    attempts=5

    while attempts>0:
        guess = input("enter your guess:")
        if not guess :
            print ("invalid input !!, please enter a valid word ")
            continue
        if guess== chosen_word:
            print ("congratulations!!! you guessed the orignal word")
            break
        else:
            attempts -=1
            if attempts>0:
                print(f"incorrect!! try again. you still have {attempts} attempts left")
            else:
                print(f"you are out of attempts !! the orignal word was {chosen_word}.")

word_scrambled_game()  

