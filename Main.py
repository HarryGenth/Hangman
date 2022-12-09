#will eventually add a random word compeont for a 5 word sorted dicitonary, for this case we are just going to use a given single word


def main():
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

    def start_q():
        global play
        play = input("Would you like to play another time?, yes = yes no = no")
        while play not in ["yes", "no", "Yes", "No"]:
            play = input("Would you like to play another time?, yes = yes no = no")
        if play == "yes" or "Yes":
            main()
        elif play == "no" or "No":
            print("Thank you very much for playing")

    def hang():
        global numb
        global length
        global word
        global prev_guess
        global play
        global ill
        lim = 5 # limit to number of guesses, limbs added each time
        guess = input("The word is: " + ill + "Please type a letter to guess: ")
        if len(guess) == 0 or len(guess) >= 2 or guess <= "9": #this makes sure the guess is a letter
            print("Invalid input")
            hang()

        elif guess in word:
            prev_guess.extend([guess])
            index = word.find(guess)
            word = word[:index] = "_" + word[index + 1:]
            ill = ill[:index] + guess + ill[index + 1:]
            print(ill)

        elif guess in prev_guess:
            print("Use a different letter")

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

            elif numb == 5:
                print("Wrong guess. You lose!")
                print("The word was", word)
                start_q()

            if word == "_" * length:
                print("Well done, youve guessd the word")
                start_q()

            elif numb != lim:
                hang()

        main()

        hang()













