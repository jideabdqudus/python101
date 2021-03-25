MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

def user_question():
    """"Ask User Coffee Choice"""
    return input('What would you like? (espresso/latte/cappuccino): ')

def collect_money():
    print("Please Insert Coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    quarters_amount = 0.25 * quarters
    dimes_amount = 0.10 * dimes
    nickles_amount = 0.05 * nickles
    pennies_amount = 0.01 * pennies

    total_amount = quarters_amount + dimes_amount + nickles_amount + pennies_amount

    pennies = "%.2f" % total_amount

    return float(pennies)



def user_prompt():
    """Prompt user what he wants to do"""

    # JSON VARIABLES FROM MENU
    espresso_water = MENU["espresso"]["ingredients"]["water"]
    espresso_coffee = MENU["espresso"]["ingredients"]["coffee"]
    espresso_cost = MENU["latte"]["cost"]

    latte_water = MENU["latte"]["ingredients"]["water"]
    latte_coffee = MENU["latte"]["ingredients"]["coffee"]
    latte_milk = MENU["latte"]["ingredients"]["milk"]
    latte_cost = MENU["latte"]["cost"]

    cappuccino_water = MENU["cappuccino"]["ingredients"]["water"]
    cappuccino_coffee = MENU["cappuccino"]["ingredients"]["coffee"]
    cappuccino_milk = MENU["cappuccino"]["ingredients"]["milk"]
    cappuccino_cost = MENU["cappuccino"]["cost"]

    total_water = espresso_water + latte_water + cappuccino_water
    total_coffee = espresso_coffee + latte_coffee + cappuccino_coffee
    total_milk = latte_milk + cappuccino_milk
    total_cost = espresso_cost + latte_cost + cappuccino_cost

    acrued_money = 0

    repeat = True
    while repeat:
        choice = user_question()
        if choice == "espresso":
            if espresso_water > total_water:
                print("Sorry there's not enough water")
            elif espresso_coffee > total_coffee:
                print("Sorry there's not enough coffee")
            else:
                total_pennies = collect_money()
                if total_pennies > espresso_cost or total_pennies == espresso_cost:
                    acrued_money += espresso_cost
                    change = float(total_pennies - espresso_cost)
                    change_dec = "%.2f" % change
                    total_water -= espresso_water
                    total_coffee -= espresso_coffee
                    print(f"Here is ${change_dec} in change")
                    print("Here's your order of ☕ Espresso")
                else:
                    print("Sorry that's not enough money. Money refunded.")
        elif choice == 'latte':
            if latte_water > total_water:
                print("Sorry there's not enough water")
            elif latte_coffee > total_coffee:
                print("Sorry there's not enough coffee")
            elif latte_milk > total_milk:
                print("Sorry there's not enough milk")
            else:
                total_pennies = collect_money()
                if total_pennies > latte_cost or total_pennies == latte_cost:
                    acrued_money += latte_cost
                    change = float(total_pennies - latte_cost)
                    change_dec = "%.2f" % change
                    total_water -= latte_water
                    total_coffee -= latte_coffee
                    total_milk -= latte_milk
                    print(f"Here is ${change_dec} in change")
                    print("Here's your order of ☕ Latte")
                else:
                    print("Sorry that's not enough money. Money refunded.")

        elif choice == 'cappuccino':
            if cappuccino_water > total_water:
                print("Sorry there's not enough water")
            elif cappuccino_coffee > total_coffee:
                print("Sorry there's not enough coffee")
            elif cappuccino_milk > total_milk:
                print("Sorry there's not enough milk")
            else:
                total_pennies = collect_money()
                if total_pennies > latte_cost or total_pennies == cappuccino_cost:
                    acrued_money += cappuccino_cost
                    change = float(total_pennies - cappuccino_cost)
                    change_dec = "%.2f" % change
                    total_water -= cappuccino_water
                    total_coffee -= cappuccino_coffee
                    total_milk -= cappuccino_milk
                    print(f"Here is ${change_dec} in change")
                    print("Here's your order of ☕ Cappuccino")
                else:
                    print("Sorry that's not enough money. Money refunded.")

        elif choice == 'report':
            print(f"Water: {total_water}ml\nMilk: {total_milk}ml\nCoffee: {total_coffee}g\nMoney: ${acrued_money}")
        elif choice == 'off':
            repeat = False
        else:
            print("Wrong Input, Start Application again")
            repeat = False


def coffee_starts():
    user_prompt()


coffee_starts()

# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”

# a. Check the user’s input to decide what to do next.
# b. The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer.

# TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
# a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
# the machine. Your code should end execution when this happens.
# if choice == "off":
#     repeat = False

# TODO:3. Print report.
# a. When the user enters “report” to the prompt, a report should be generated that shows
# the current resource values. e.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# if choice == "report":
#     repeat = False
#     print(f'Water: {resources["water"]}ml\nMilk: {resources["water"]}ml\nCoffee: {resources["coffee"]}g\n Money: ${money}')

# TODO:4. Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough
# resources to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
# not continue to make the drink but print: “Sorry there is not enough water.”
# c. The same should happen if another resource is depleted, e.g. milk or coffee.


# TODO: 5. Process coins.
# a. If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

# TODO: 6. Check transaction successful?
# a. Check that the user has inserted enough money to purchase the drink they selected.
# E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
# program should say “Sorry that's not enough money. Money refunded.”.
# b. But if the user has inserted enough money, then the cost of the drink gets added to the
# machine as the profit and this will be reflected the next time “report” is triggered. E.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# c. If the user has inserted too much money, the machine should offer change.
# E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
# places.

# TODO: 7. Make Coffee.
# a. If the transaction is successful and there are enough resources to make the drink the
# user selected, then the ingredients to make the drink should be deducted from the
# coffee machine resources.
# E.g. report before purchasing latte:
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0
# Report after purchasing latte:
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
# latte was their choice of drink.