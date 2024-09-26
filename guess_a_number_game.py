import random
choosen_number = random.randint(0,100)
players_guess = "opps an error has acorred"
ranvar = 0
game_start = input("Hello player do you want to play guess a number?: Y/N")
if game_start == "y" or game_start == "y":
    while ranvar == 0:
        player_input = int(input("Please choose a number from 0 to 100: "))
        if player_input == choosen_number:
            print("It's your lucky day\nYou guessed the correct number")
            ranvar = ranvar + 5
        elif player_input > choosen_number:
            print("The number is lower")
            print("Try again")
        elif player_input < choosen_number:
            print("The number is higher")
            print("Try again")
        else:
            print("Please enter a number in range of 0 to 100")
else:
    print("OK Have a nice day")