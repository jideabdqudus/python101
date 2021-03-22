import random


def black_jack_game():
    print(f"Welcome to the BlackJack Game \n")

    cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    user_first_pick = random.choice(cards)
    user_second_pick = random.choice(cards)
    user_list = [user_first_pick, user_second_pick]
    sum_of_user_list = sum(user_list)

    computer_first_pick = random.choice(cards)
    computer_second_pick = random.choice(cards)
    computer_list = [computer_first_pick, computer_second_pick]
    sum_of_computer_list = sum(computer_list)


    should_continue = True

    while should_continue:
        if sum_of_computer_list == 21:
            print("You lose")
            print(f"Computer dealt: {computer_list}")
            should_continue = False
            black_jack_game()
        elif sum_of_user_list == 21:
            print("You Win")
            print(f"You dealt: {user_list}")
            should_continue = False
            black_jack_game()
        elif sum_of_user_list == 21 and sum_of_computer_list == 21:
            print("You lose")
            print(f"Computer dealt: {computer_list}")
            should_continue = False
            black_jack_game()

        print(f"Your cards: {user_list}")

        print(f"Computer's first card: {computer_first_pick}")

        decision = input("Type 'y' to get another card, type 'n' to pass: ")

        if decision == "y":
            user_third_pick = random.choice(cards)
            if user_third_pick == 11 and sum_of_user_list > 10:
                user_third_pick == 1
                user_list.append(user_third_pick)
                sum_of_user_list = sum(user_list)
            else:
                user_list.append(user_third_pick)
                sum_of_user_list = sum(user_list)

            computer_third_pick = random.choice(cards)

            if computer_third_pick == 11 and sum_of_computer_list > 10:
                computer_third_pick == 1
                computer_list.append(computer_third_pick)
                sum_of_computer_list = sum(computer_list)
            else:
                computer_list.append(computer_third_pick)
                sum_of_computer_list = sum(computer_list)

            if sum_of_user_list > 21:
                print("You lose")
                print(f"You dealt a sum value higher than 21, {user_list}")
                print("\n")
                should_continue = False
                black_jack_game()
            else:
                if sum_of_user_list > sum_of_computer_list:
                    print("You win")
                    print(f"Computer dealt {computer_list}, and you dealt {user_list}")
                    print(f"Sum of Computer list is: {sum_of_computer_list} ,Sum of User list is:  {sum_of_user_list}")
                    print("\n")
                    should_continue = False
                    black_jack_game()
                elif sum_of_user_list == sum_of_computer_list:
                    print("You tie")
                    print(f"Computer dealt {computer_list}, and you dealt {user_list}")
                    print(f"Sum of Computer list is: {sum_of_computer_list} ,Sum of User list is:  {sum_of_user_list}")
                    print("\n")
                    should_continue = False
                    black_jack_game()
                else:
                    print("You lose")
                    print(f"Computer dealt {computer_list}, and you dealt {user_list}")
                    print(f"Sum of Computer list is: {sum_of_computer_list} ,Sum of User list is:  {sum_of_user_list}")
                    print("\n")
                    should_continue = False
                    black_jack_game()
        elif decision == "n":
            print(f"Your final hand: {user_list}")
            print(f"Computer's final hand: {computer_list}")
            if sum_of_user_list > sum_of_computer_list:
                print("You win")
                print("\n")
                should_continue = False
                black_jack_game()
                print("\n")
            else:
                print("You lose")
                print("\n")
                should_continue = False
                black_jack_game()
                print("\n")

        else:
            print("Please make a right choice next time")
            print("\n")
            should_continue = False
            black_jack_game()
            print("\n")

print("Test Commit")

black_jack_game()
