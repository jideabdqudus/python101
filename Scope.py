############SCOPE##############

import random

"""
enemies = 1  #Global Variable


def increase_enemies():
    global enemies
    enemies += 1     #Local Variable
    print(f"Enemies inside function is now {enemies}")


increase_enemies()
print(f"Enemies from outside function is now {enemies}")
"""

WELCOME_MESSAGE = "Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100. \n"

randomized_number = random.randint(1, 100)


def numberGuess():
    print(WELCOME_MESSAGE)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    easy_difficulty = 10
    hard_difficulty = 5

    if difficulty == "easy":
        print(f"You have {easy_difficulty} attempts remaining to guess the number")





numberGuess()

