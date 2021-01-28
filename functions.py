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


def playRps():
    global quitGame
    quitGame = ""

    if playerAction == "r" and computerAction == "r":
        tied()
    elif playerAction == "r" and computerAction == "p":
        playerLoss()
    elif playerAction == "r" and computerAction == "s":
        playerWin()
    elif playerAction == "p" and computerAction == "r":
        playerWin()
    elif playerAction == "p" and computerAction == "p":
        tied()
    elif playerAction == "p" and computerAction == "s":
        playerLoss()
    elif playerAction == "s" and computerAction == "r":
        playerLoss()
    elif playerAction == "s" and computerAction == "p":
        playerWin()
    elif playerAction == "s" and computerAction == "s":
        tied()
    elif playerAction == "q":
        quitGame = True
    else:
        print("Unknown input.")
