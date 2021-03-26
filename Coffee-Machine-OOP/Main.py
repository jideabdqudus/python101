from menu import Menu, MenuItem
from CoffeeMaker import CoffeeMaker
from MoneyMachine import MoneyMachine

#Create an accessible object out of each class
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

#Set looping condition for the coffee machine
is_on = True

while is_on:
    options = menu.get_items() #Gets the list of items in the menu
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        is_enough_ingredients = coffee_maker.is_resource_sufficient(drink)
        is_payment_successful = money_machine.make_payment(drink.cost)
        if is_enough_ingredients and is_payment_successful:
            coffee_maker.make_coffee(drink)