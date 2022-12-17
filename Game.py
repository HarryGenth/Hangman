import random
from VLibs import Pres # All of these import the VLibs from the VLibs.py module.
from VLibs import MLB # This simply saves space on this main Game.py module
from VLibs import Mam
from VLibs import FF
from VLibs import Moods
from VLibs import Shoes
from VLibs import Dict

#The below list is a collection of illustrarions depicting each stage in the hangman game
hangman_art = [""" 
    +---+
        |
        |
        |
       ===""","""
    +---+
    O   |
        |
        |
       ===""","""
    +---+
    O   |
    |   |
        |
       ===""","""
    +---+
    O   |
   \|   |
        |
       ===""","""
    +---+
    O   |
   \|/  |
        |
       ===""","""
    +---+
    O   |
   \|/  |
   /    |
       ===""","""
    +---+
    O   |
   \|/  |
   / \  |
       ===""","""
    +---+
    O   |
   \|/  |
   / \  |
       ===
    They Died!"""]



def start_q(): #This start q function is the end of game UI
    play = input("Would you like to play another time?, yes = yes no = no")
    if play == "yes":
        return choose(hidden)
    elif play == "no":
        print("Thank you very much for playing")
    else:
        print("Invalid input, please type yes or no if you'd like to play again")
        return start_q()

def choose(hidden): #this function runs the initial UI that lets the user choose between several different themes libraries
    option = input("Choose a theme: (1)English Dictionary, (2) MLB Teams (3)US Presidents, (4)Mammals, (5)Fast Food Restaurants, (6)Moods, (7)Shoe Brands. Type 1, 2, 3, 4, 5, 6, or 7")
    if option == "1":
        print("You've selected English Dictionary. Note that each answer is only one word and all lowercase")
        word_list = Dict #"word_list" identifies the theme choses and allows a random term to be chosen from it later on
    elif option == "2":
        print("Youv'e selected MLB Teams. Note that each answer is simply the mascot name (orioles, yankees, redsox), are one word and all lowercase")
        word_list = MLB
    elif option == "3":
        print("You've selected US Presidents. Note that each answer is only the presidents last name (vanburen, bush, mckinley), and all letters are lowercase.")
        word_list = Pres
    elif option == "4":
        print("You've selected Mammals. Note that each answer is only one word and all letters are lowercase (bear, donkey, horse)")
        word_list = Mam
    elif option == "5":
        print("You've selected Fast Food restaurants. Note that each answer is only one word and all lowercase (kfc, tacobell, mcdonalds, chickfila)")
        word_list = FF
    elif option == "6":
        print("You've selected Moods. Note that each mood is one word with all lowercase letters (happy, sad)")
        word_list = Moods
    elif option == "7":
        print("You've selected Shoes. Note that each answer is one word and only has lowercase letter (underarmour, nike, adidas)")
        word_list = Shoes
    else:
        print("invalid input, please type either 1, 2, 3, 4, 5, 6, or 7 based on what theme you'd like to choose")
        return choose
    hidden = random.choice(word_list) #hidden is the var for the randomly selected word out of the chosen lsit
    return hidden

print("Hello, Thank you for playing  Harry's Hangman game\n") # welcome outside of choose function so it is not re-printed
name = input("What is your name?: ")
print("Hi", name, "Good luck\n")

#identifies hidden term to be used in several functions
hidden = ''
hidden = choose(hidden)

#Starts display w underscores for the letters in the hidden word
display = ['_' for letter in hidden]

#The following lists track correct and incorrect guesses
correct_guesses = [ ]
incorrect_guesses = [ ]
max_incorrect_guesses = 7 #limit to how many incorrect guesses the user is allowed before they lose
#once the incorrect guesses count = this the game ends

incorrect_guesses_count = 0 #start at 0
while True:
    print(' '.join(display))
    print(hangman_art[incorrect_guesses_count])

    guess = input("Guess a letter: ").lower() #The .lower automatically changes the input to lower case to take account of the user inputting an uppercase letter

    alph = set("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM") #this set defines all the alowed inputs

    if guess not in alph:
        print("Invalid input") #invalid input message sent to the user

    elif guess in hidden: #checks to see if the guess is in the word and if it is then it displays it on the '_'
        for i in range(len(hidden)):
            if hidden[i] == guess:
                display[i] = guess
    elif guess in incorrect_guesses: #this function accounts for incorrect letters the user has already guessed.
            print("You've already guessed that letter")
    else:
        incorrect_guesses.append(guess) #this adds an incorrect guess to the list of previsouly guessed incorrect letters
        incorrect_guesses_count += 1 #adds 1 to the count of incorrect guesses
        print("These letters are not in the word", incorrect_guesses) #display for precisouly guessed letters
    if '_' not in display: #if there are no blanks left in the display, the user won the game
        print("You won")
        print("The word was", hidden)
        start_q()
    elif incorrect_guesses_count == max_incorrect_guesses: #user loses the game
        print("You lost!")
        print("The word was", hidden)
        start_q()
        break




























