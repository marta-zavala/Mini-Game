from src.games import game_type, player_guess, computer_guess, play_again
import random

print("---- Let's play Guess The Number ----")

play = 'Y'

while play == 'y' or play == 'Y':
    game_type()
    play = play_again()

print("\nGoodbye! Hope you enjoyed the game :)")