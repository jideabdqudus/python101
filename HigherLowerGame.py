# Import game Logo
from art import higher_lower_logo
from HigherLowerData import data
from random import randint
from art import higher_lower_vs

print(higher_lower_logo)

def correct_scores():


value_a = data[randint(1, 50)]
name_a = value_a["name"]
description_a = value_a["description"]
country_a = value_a["country"]
follower_count_a = value_a["follower_count"]

# Compare person A
print(f"Compare A: {name_a}, a {description_a}, from {country_a}.")

# VS
print(higher_lower_vs)

# Compare with person B
value_b = data[randint(1, 50)]
name_b = value_b["name"]
description_b = value_b["description"]
country_b = value_b["country"]
follower_count_b = value_b["follower_count"]

print(f"Against B: {name_b}, a {description_b}, from {country_b}.")

# Receive input of users choice A/B
user_input = input("Who has more followers? Type 'A' or 'B': ")

# If correct, print You're right and correct score

if user_input == "A" and follower_count_a > follower_count_b:
    print("You're right")
elif user_input == "B" and follower_count_b > follower_count_a:
    print("You're right")
elif user_input == "A" and follower_count_b > follower_count_a:
    print("You're wrong")
elif user_input == "B" and follower_count_b < follower_count_a:
    print("You're wrong")
else:
    print("Choose a valid response")

# If wrong, end game and print correct score

# IF correct, delete A, leave B and compare B to next B

# Take while loop in coverage