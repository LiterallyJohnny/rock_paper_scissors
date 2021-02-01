# This file contains many functions to be used in the main file

import random  # Allows randomizing things such as lists and strings

# List of valid choices when the player is asked for their choice
possibleChoices = (
    "r",  # Rock
    "p",  # Paper
    "s",  # Scissors
)

# The player's and the computer's starting scores
playerScore = 0
computerScore = 0


def addPointPlayer():  # Adds a point for the player
    global playerScore
    playerScore = playerScore + 1


def addPointComputer():  # Adds a point for the computer
    global computerScore
    computerScore = computerScore + 1


def scores():  # Retreives the scores and prints them
    print("Player's score: " + str(playerScore))
    print("Computer's score: " + str(computerScore))


def playerLoss():  # Response if the player loses
    addPointComputer()
    print("You lost! One point to the computer!")
    scores()


def playerWin():  # Response if the player wins
    addPointPlayer()
    print("You won! One point to you!")
    scores()


def tied():  # Response if the player and the computer ties
    print("Tied! No points awarded.")


def playerChoice():  # Asks the player for their choice
    global playerAction

    playerAction = input(
        """
    Rock, paper, or scissors?
    Acceptable responses are...
    "r": Chooses rock.
    "p": Chooses paper.
    "s": Chooses scissors.

    "q": Quits the game.
    """
    )


def computerChoice():  # Gives the computer a random choice from the possibleChoices list
    global computerAction
    computerAction = random.choice(possibleChoices)
    computerAction = computerAction


def playRps():  # Compares the choices and determines who won the game
    game = "".join([playerAction, computerAction])

    outcomes = {
        "rr": tied,
        "pp": tied,
        "ss": tied,
        "rp": playerLoss,
        "ps": playerLoss,
        "sr": playerLoss,
        "rs": playerWin,
        "pr": playerWin,
        "sp": playerWin,
    }

    if playerAction == "q":
        return False
    else:
        action = outcomes.get(game)
        if action:
            action()
        else:
            print("Invalid input!")
