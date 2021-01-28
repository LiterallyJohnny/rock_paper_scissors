import random  # Allows randomizing things such as lists and strings
import functions  # Imports the functions.py file

# Asks the player if they would like to play rps. If yes, the program will continue onto the next loop.
while True:
    playRps = str(input('Would you like to play "Rock, Paper, Scissors"? (Y/n): '))

    if playRps == "y":
        while True:
            functions.playGame()

    elif playRps == "n":
        print("Terminating program...")
        quit()

    else:
        print("Unknown input. Please enter a valid answer.")
        continue