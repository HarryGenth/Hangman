import random
from Game import path
from Game import start_q
from Game import choice




def hang():
    path()
    global numb
    global length

    global prev_guess
    global play


    numb = 0
    length = len(random.choice(choice))
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
            return start_q
    if word == "_" * length:
            print("Well done, youve guessd the word")
            return start_q()
    elif numb != lim:
            hang()
hang()




















