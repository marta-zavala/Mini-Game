import random

def game_type():
    option = input("Choose an option (1 or 2):\n   1. Computer Guess\n   2. Player Guess\n")
    while option !='1' and option != '2':
        print("ERROR: You must introduce one option, 1 or 2.")
        option = input("Choose an option (1 or 2):\n   1. Computer Guess\n   2. Player Guess\n")
    if option == '1':
        print("\n\n---- Computer guess. Let's start! ----\n")
        computer_guess()
    else:
        print("\n\n---- Player guess. Let's start! ----\n")
        player_guess()

def play_again():
    play = input("\nDo you want to play again? (Y/N): ")
    while play not in ['Y','y','N','n']:
        play = input("\nERROR: You must introduce Y or N.\nDo you want to play again? (Y/N): ")
    return play

def player_guess():
    # The computer generates a random number
    print("The computer is going to generate a random number between 1 and 100...")
    num = random.randint(1,100)
    sol = 0
    cont = 0
    # The player guess
    while sol != num:
        sol = input("What number has the computer chosen?\n")
        try:
            sol = int(sol)
            cont += 1
            if sol>num:
                print("The chosen number is less than yours. Try again!\n")
            elif sol<num:
                print("The chosen number is greater than yours. Try again!\n")
            else:
                print(f"You got it right after {cont} tries!\n")
        except:
            print("ERROR: You must introduce a number. Remember that the chosen one is between 1 and 100\n")


def computer_guess():
    # The player choose a number between 1 and 100
    num = 0
    while num not in range(1,101):
        num = input("Choose a number between 1 and 100:\n")
        try:
            num = int(num)
            if num not in range (1,101):
                num = 0
                print("The chosen number must be between 1 and 100. Try again.\n")
        except:
            print("You must introduce a number not a character. Try again.\n")
    #The computer guess
    cont = 1
    minim = 1
    maxim = 100
    sol = random.randint(minim, maxim)
    print(f"The chosen number is {sol}\n")
    while sol != num:
        cont += 1      
        ans = input("   Is your number higher or lower (H/L)?: ")  
        # Check in case the user enters the option wrong
        while ans not in 'HhLl':
            ans = input("       Your answer must be 'H' or 'L'. Please, enter it again: ")
        # What happens if the guess is higher or lower? The computer change the min and max option of the range
        if ans == 'H' or ans == 'h':
            minim = sol
            print("   The choosen number is greter than yours. Try again!\n")
        else:
            maxim = sol
            print("   The choosen number is less than yours. Try again!\n")
        # I create a check so that if the new number generated is the same as the previous one, I know that the user has lied
        check = sol
        sol = int((maxim+minim)/2)
        if check == sol:
            print("-> I can't figure out the number because you cheated!\n")
            break
        else:
            print(f"The chosen number is {sol}\n")
    if num == sol:
        print(f"-> The computer got it right after {cont} tries!")