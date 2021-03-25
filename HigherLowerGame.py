# Import game Logo
from art import higher_lower_logo, higher_lower_vs
from HigherLowerData import data
from random import randint, choice


def get_random_account():
    """Get Random Account in List"""
    return data[randint(1, 49)]


def person(value):
    name = value["name"]
    description = value["description"]
    country = value["country"]
    follower_count_a = value["follower_count"]
    return f"{name}, a {description}, from {country}."

def person_b():
    value_b = data[randint(1, 50)]
    name_b = value_b["name"]
    description_b = value_b["description"]
    country_b = value_b["country"]
    follower_count_b = value_b["follower_count"]
    return f"{name_b}, a {description_b}, from {country_b}."

# Receive input of users choice A/B

def check_guess(guess, follower_count_a, follower_count_b):
    """Checks followers against user's guess
    and returns True if they got it right.
    Or False if they got it wrong."""
    if follower_count_a > follower_count_b:
        return guess == "a"
    else:
        return guess == "b"


def start_game():

    print(higher_lower_logo)
    score = 0
    should_continue = True
    account_a = get_random_account()
    account_b = get_random_account()

    while should_continue:
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()
        print(f"Compare A: {person(account_a)}.")
        print(higher_lower_vs)
        print(f"Against B: {person(account_b)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_guess(guess, a_follower_count, b_follower_count)
        print(higher_lower_logo)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")

    # If correct, print You're right and correct score



# If wrong, end game and print correct score

# IF correct, delete A, leave B and compare B to next B

# Take while loop in coverage

start_game()

