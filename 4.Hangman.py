# HANGMAN

import random

def takeGuesses(guessesIn):
    global healthsLeft
    letterIn = input("Make a guess: ").lower().strip()
    if len(letterIn)==1:
        same = 0
        for letter in guessesIn:
            if letter == letterIn:
                same+=1
        if same==0:
            guessesIn.append(letterIn)
            return True
        else:
            print("You already made this guess.")
            return False
    else:
        print("Please only enter one letter.")
        takeGuesses(guessesIn)
    return False

def compare(wordIn,guessesIn):
    global run
    global healthsLeft
    underScore = 0
    for letter1 in wordIn:
        same = 0       
        for letter2 in guessesIn:
            if letter1==letter2:
                same+=1
        if same==0:
            print('_')
            underScore+=1
        else:
            print(letter1)
    if underScore==0:
        run = False

WordBank = ['baby', 'katherine', 'mehmet', 'brandt', 'university', 'trashplace', 'shit','isdoneinbathroom','yeahsure']

def endGame():
    answer = input("Do you want to play again?")

    if answer.lower().strip() == 'yes':
        GameMenu()
    elif answer.lower().strip() == 'no':
        print("See you again!")
    else:
        print("Please enter a valid answer.")
        endGame()

def Game():
    global run
    global healthsLeft

    print("Welcome to the Hangman!")
    word = random.choice(WordBank)
    guesses = []
    print("The word has",len(word),"letters.")

    run = True
    healthsLeft = 9

    while run:
        if takeGuesses(guesses):
            compare(word,guesses)
    
def GameMenu():   
    Game()

    print("Game Over!")
    endGame()

GameMenu()
