#will eventually add a random word compeont for a 5 word sorted dicitonary, for this case we are just going to use a given single word
from english_words import english_words_set
from VLibs import MLB
from VLibs import Pres
global lib
global theme
from Game import t

print("Hello, Thank you for playing  Harry's Hangman game\n")
name = input("What is your name?: ")
print("Hi", name, "Good luck")
path = input("Would you like to play with random words, or choose a theme? Please type r for random and t for theme: ")
    if path == "r" or "R":
        lib = english_words_set
    elif path == "t" or "T":
        print("Please choose from one of the following themes: MLB Baseball teams (MLB), US Presidents (US), Fast-Food Chains (FF), Famous Poets (FP), Popular Brands (PB)"))
        theme = input("Please select your choice by typing MLB, US, FF, FP,or PB based on the above options: ")
            if theme == "MLB":
                print("The generated MLB team will be the mascot ie: Orioles, Redsox, Whitesox, Cardinals etc. The hometown is not included and all answers are oneword with the first letter capitalized")
                lib = MLB
                return
            elif theme == "Pres":
                print("The generated Hangman word will be ")

def Main():
    global numb #naming all global vars and inputting each
    global length
    global word
    global prev_guess
    global play
    global ill
    word = random.randint(0, len(lib) - 1)
    numb = 0
    length = len(word)
    ill= "_" * length
    prev_guess = []
    play = ""

def start_q():
    global play
    play = input("Would you like to play another time?, yes = yes no = no")
    while play not in ["yes", "no", "Yes", "No"]:
        play = input("Would you like to play another time?, yes = yes no = no")
        if play == "yes" or "Yes":
            return Main()
        elif play == "no" or "No":
            print("Thank you very much for playing")

def hang():
    global numb
    global length
    global word
    global prev_guess
    global play
    global ill
    word = "Chair"
    numb = 0
    length = len(word)
    ill = "_" * length
    prev_guess = []
    play = ""
    lim = 5 # limit to number of guesses, limbs added each time
    guess = input("The word is: " + ill + "Please type a letter to guess: ")
    if len(guess) == 0 or len(guess) >= 2 or guess <= "9": # this makes sure the guess is a letter
        print("Invalid input")
        hang()
    elif guess in word:
        prev_guess.extend[guess]
        index = word.find(guess)
        word = word[index] = "_" + word[index + 1]
        ill = ill + word.find(index) + 1
        print(ill)

    elif guess in prev_guess:
        print("Use a different letter")
#following code is for differing responses based on previous incorrect guesses
    else:
        numb += 1

        if numb == 1:
            print("Wrong guess. " + str(lim - numb) + "guesses left")

        elif numb == 2:
            print("Wrong guess. " + str(lim - numb) + "guesses left")

        elif numb == 3:
            print("Wrong guess. " + str(lim - numb) + "guesses left")

        elif numb == 4:
            print("Wrong guess. " + str(lim - numb) + "guesses left")

        elif numb == 5: #user loses the game
            print("Wrong guess. You lose!")
            print("The word was", word)
            start_q()
    if word == "_" * length:
            print("Well done, youve guessd the word")
            start_q()
    elif numb != lim:
            hang()
Main()

hang()



















