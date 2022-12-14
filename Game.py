import random
from VLibs import Pres
from VLibs import MLB
from VLibs import Mam
from VLibs import FF
from VLibs import Moods
from VLibs import Shoes
from VLibs import Dict
global word



print("Hello, Thank you for playing  Harry's Hangman game\n") # welcome outside of path function so it is not re-printed
name = input("What is your name?: ")
print("Hi", name, "Good luck\n")

def path():
    option = input("Choose a theme: (1)English Dictionary, (2) MLB Teams (3)US Presidents, (4)Mammals, (5)Fast Food Restaurants, (6)Moods, (7)Shoe Brands. Type 1, 2, 3, 4, 5, 6, or 7")
    if option == "1":
        print("You've selected English Dictionary. Note that each answer is only one word and all lowercase")
        list = Dict
    elif option == "2":
        print("Youv'e selected MLB Teams. Note that each answer is simply the mascot name (orioles, yankees, redsox), are one word and all lowercase")
        list = MLB
    elif option == "3":
        print("You've selected US Presidents. Note that each answer is only the presidents last name (vanburen, bush, mckinley), and all letters are lowercase.")
        list = Pres
    elif option == "4":
        print("You've selected Mammals. Note that each answer is only one word and all letters are lowercase (bear, donkey, horse)")
        list = Mam
    elif option == "5":
        print("You've selected Fast Food restaurants. Note that each answer is only one word and all lowercase (kfc, tacobell, mcdonalds, chickfila)")
        list = FF
    elif option == "6":
        print("You've selected Moods. Note that each mood is one word with all lowercase letters (happy, sad)")
        list = Moods
    elif option == "7":
        print("You've selected Shoes. Note that each answer is one word and only has lowercase letter (underarmour, nike, adidas)")
        list = Shoes
    else:
        print("invalid input, please type either 1, 2, 3, 4, 5, 6, or 7 based on what theme you'd like to choose")
        return path()
    word = random.choice(list)
    print(word)
    return hang

def start_q():
        play = input("Would you like to play another time?, yes = yes no = no")
        if play == "yes":
            return path()
        elif play == "no":
            print("Thank you very much for playing")
        else:
            print("Invalid input, please type yes or no if you'd like to play again")
            return start_q()

def hang():
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
            return hang
        elif numb == 2:
            print("Wrong guess. " + str(lim - numb) + "guesses left")
            return hang
        elif numb == 3:
            print("Wrong guess. " + str(lim - numb) + "guesses left")
            return hang
        elif numb == 4:
            print("Wrong guess. " + str(lim - numb) + "guesses left")
            return hang
        elif numb == 5: #user loses the game
            print("Wrong guess. You lose!")
            print("The word was", word)
            return start_q
    if word == "_" * length:
            print("Well done, youve guessd the word")
            return start_q()
    elif numb != lim:
            hang()

#path is the UI used to select the theme and give basic instructions regarding the game

path()







