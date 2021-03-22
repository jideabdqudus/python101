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
        print(f'You have {easy_difficulty} attempts remaining to guess the number')

        the_num = randomized_number

        user_input = int(input("Make a guess: "))


        if easy_difficulty > 0:
            should_continue = True
            while should_continue:
                if user_input < the_num:
                    print(f"Too low.\nGuess again.")
                    easy_difficulty - 1
                    print(f'You have {easy_difficulty} attempts remaining to guess the number')
                elif user_input > the_num:
                    print(f"Too high.\nGuess again.")
                    easy_difficulty - 1
                    print(f'You have {easy_difficulty} attempts remaining to guess the number')
                else:
                    print(f"You got it the answer was {the_num}")
        else:
            should_continue = False






#numberGuess()


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

#Make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():

  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = random.randint(1, 100)
  print(f"Pssst, the correct answer is {answer}")

  turns = set_difficulty()
  #Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    #Let the user guess a number.
    guess = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")


game()


