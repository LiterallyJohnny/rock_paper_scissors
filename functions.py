# This file contains many functions to be used in the main file

import random  # Allows randomizing things such as lists and strings

possibleChoices = (
    "r",
    "p",
    "s",
)

playerScore = 0
computerScore = 0


def addPointPlayer():
    global playerScore
    playerScore = playerScore + 1


def addPointComputer():
    global computerScore
    computerScore = computerScore + 1


def scores():
    print("Player's score: " + str(playerScore))
    print("Computer's score: " + str(computerScore))


def playerLoss():
    addPointComputer()
    print("You lost! One point to the computer!")
    scores()


def playerWin():
    addPointPlayer()
    print("You won! One point to you!")
    scores()


def tied():
    print("Tied! No points awarded.")


def playerChoice():
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


def computerChoice():
    global computerAction
    computerAction = random.choice(possibleChoices)
    computerAction = computerAction


def playRps():
    game = "".join([playerAction, computerAction])
    global quitGame

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
        quitGame = True  # TODO: Figure out why this isn't working in the main.py file
    else:
        action = outcomes.get(game)
        if action:
            action()
        else:
            print("Invalid input!")
