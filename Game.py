import random
from VLibs import Pres
from VLibs import MLB
from VLibs import Mam
from VLibs import FF
from VLibs import Moods
from VLibs import Shoes
#These are the themes
def path():
    choice = list
    option = input("Choose a theme: (1)English Dictionary, (2) MLB Teams (3)US Presidents, (4)Mammals, (5)Fast Food Restaurants, (5)Moods, (6)Shoe Brands, (7)English Dictionary   ")
    if option == "1":
        print("You've selected English Dictionary. Note that each answer is only one word and all lowercase")
    elif option == "2":
        print("Youv'e selected MLB Teams. Note that each answer is simply the mascot name (Orioles, Yankees, Redsox), are one word and all lowercase")
        choice = MLB
    elif option == "3":
        print("You've selected US Presidents. Note that each answer is only the presidents last name (vanburen, bush, mckinley), and all letters are lowercase.")
        choice = Pres
    elif option == "4":
        print("You've selected Mammals. Note that each answer is only one word and all letters are lowercase (bear, donkey, horse)")
        choice = Mam
    elif option == "5":
        print("You've selected Fast Food restaurants. Note that each answer is only one word and all lowercase (kfc, tacobell, mcdonalds, chickfila ")
        choice = FF
    elif option == "6":
        print("You've selected Moods. Note that each mood is one word with all lowercase letters (")
        choice = Moods
    elif option == "7":
        print("You've selected Shoes. Note that each answer is one word and only has lowercase letter (underarmour, nike, adidas)")
        choice = Shoes

    else:
        print("invalid input")
        return path()
    print(choice)

path()




