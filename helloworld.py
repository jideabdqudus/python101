# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 14:38:39 2020

@author: adbul-qudus.olajide
"""

"""
print("Where are you from?")
state = input()
print ("What's your pets name?")
pet = input()
print("Suggested stadium name is..")
print(state + " " + pet)


#input("What is your name?")

print("Hello " + input("What is your name"))

name = input("What is your name ")
print(len(name))


print (len(input("What is your name? ")))

name = input("What is your name ")
length = len(name)
print(length)
a: 5
b: 100
a= 100 
b=5


letterA = input("a: ")
letterB = input("b: ")
print('a = ' + letterB)
print('b = ' + letterA)


a = input("a: ")
b = input ("b: ")
c=a
a=b
b=c
print ("a = " + a)
print ("b = " + b)


print ("Welcome to the Band Name Generator")
state = input("Where are you from \n")
pet = input("What's your pets name? \n")
print("Your band name could be " + state + " " + pet )

number = input("Type a two digit number:\n")


print (int(number[0]) + int(number[1]))

##A program that tells how many days, months, weeks you have left if you life till 90 years old

age = int(input("what is your age?\n"))

days_90 = 365 * 90
weeks_90 = 52 * 90
months_90 = 12 * 90

a = days_90 - (age * 365)
b = weeks_90 - (age * 52)
c = months_90 - (age * 12)

print(f"If you live till 90 years old, you die in {a} days, {b} weeks, and {c} months :)")

if (input("What is your name? ") == "jake")   :
    print("Nice name")
else:
    print("Blehh")

number = int(input("Write your number: "))

if number % 2:
    print("odd")
else:
    print("even")




#Leap Year Checker

print ("Leap Year Checker \n ")

year = int(input("What year do you want to check? \n"))

 
if(year % 4 == 0 and year % 100 == 0 and year % 400 == 0):
    print(f"The year {year}, is a leap year")
elif(year % 4 == 0 and year % 100 != 0):
    print(f"The year {year}, is a leap year")
else:
    print(f"The year {year}, is not a leap year")


"""

"""

print ("Welcome to Pizza Factory \n")

SP : $15
MP : $20
LP : $25

Peperoni for small Pizza: +$2
Peperoni for medium or large Pizza: +$3

Extra cheese for any size of pizza: +$1

size = L
peperoni = Y
cheese = N

price = $28



print ("Welcome to the Pizza Factory \n")

pizza_size = input("What size of Pizza do you want? S, M or L \n")


if (pizza_size == "S"):
    bill = 15
    if(input("Would you like Pepperoni?  ") == "Y" or "y" or "yes" or "Yes"):
        print(f"Your Total Bill is ${bill + 2}")
        if(input("Would you like extra cheese? ") =="Y" or "y" or "yes" or "Yes"):
            print(f"Your Total Bill is {bill + 1}")
    else:
        print(f"Your bill is ${bill}")
elif (pizza_size == "M"):
    bill = 20
    if(input("Would you like Pepperoni?  ") == "Y" or "y" or "yes" or "Yes"):
        print(f"Your Total Bill is ${bill + 3}")
    else:
        print(f"Your bill is ${bill}")
elif (pizza_size == "L"):
    bill = 25
    if(input("Would you like Pepperoni?  ") == "Y" or "y" or "yes" or "Yes"):
        print(f"Your Total Bill is ${bill + 3}")  
    else:
        print(f"Your bill is ${bill}")
else:
    print("Please confirm you made the right input and then try again")
    
    
    
#Pizza Calculator

print("Welcome to Python Pizza Deliveries")

size = input("What size of Pizza do you want? S, M, or L? ")
peperoni = input("Do you want peperoni? Y or N ")
cheese = input("Do you want extra cheese? Y or N ")

bill = 0

if (size == "S"):
    bill += 15
elif (size == "M"):
    bill += 20
elif (size == "L"):
    bill += 25
    
if peperoni == "Y":
    if size == "S":
        bill += 2
    elif size == "M":
        bill += 3
    elif size == "L":
        bill += 3
else:
    bill += 0

if cheese == "Y":
    bill += 2

print(f"Your total bill is ${bill}")    


print(("Love Machine, Find out if you're a match"))


yourname = input("What's your full name? \n").lower()
partner = input("What's your Partners Full Name? \n").lower()

yourarray = list(yourname)
removed = yourarray.remove(" ")
    
partnerarray = list(partner)
comot = partnerarray.remove(" ")
    
myscore = int(len(list(filter({'t','r', 'u', 'e', 'l', 'o' 'v', 'e'}.__contains__, yourarray))))
 
partnerscore = int(len(list(filter({'t','r', 'u', 'e', 'l', 'o' 'v', 'e'}.__contains__, partnerarray))))
    

score = int(f"{myscore}{partnerscore}")

print(" ")

if score < 10 or score > 90:
    print (f"Your score is {score}, you go together like Coke and Mentos")
elif score >=40 and score <=50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")


import random

test = int(input("Create a seed number: "))

random.seed(test)

side = random.randint(0,1)

if side == 1:
    print('Heads')
else:
    print('Tails')



import random

test = int(input("Create a seed number: "))
random.seed(test)

nameAsCSV = input("What are the names, seperated by comma\n ")

names = nameAsCSV.split(",")

length = len(names)

pay = random.randint(0,length-1)

print(names[pay])



Rock Paper Sciccors

import random 


rock = 0
paper = 1
scissors = 2

field = int(input(("Pick 0,1,2. Rock, Paper, Scissors \n")))
arrayed = [rock, paper, scissors]
randomed = int(random.choice(arrayed))


if field == 0 and randomed == 2:
    print(f"You win, you pick {field}, I chose {randomed}")
elif field == 2 and randomed == 1:
    print(f"You win, you pick {field}, I chose {randomed}")
elif field == 1 and randomed == 0:
    print(f"You win, you pick {field}, I chose {randomed}")
elif field == 0 and randomed == 0:
    print(f"You draw, you pick {field}, I chose {randomed}")
elif field == 1 and randomed == 1:
    print(f"You draw, you pick {field}, I chose {randomed}")
elif field == 2 and randomed == 2:
    print(f"You draw, you pick {field}, I chose {randomed}")
else:
    print(f"You lose, you pick {field}, I chose {randomed}")


Highest Scores Game

scores = input("Input a list of student scores \n").split(" ")

for n in range (0, len(scores)):
    scores[n] = int(scores[n])
print(scores)

highest = 0

for score in scores:
 if score > highest:
  highest = score
  
print(f"The highest score is {highest}")




scores = 0

for n in range (2, 101, 2):
    scores+=n
print(scores)



# FizzBuzz

for number in range(1, 101):
    if(number % 15 == 0):
     print("fizzbuzz")
    elif(number % 5 == 0):
        print("buzz")
    elif(number % 3 == 0):
        print("fizz")
    else:
        print(number)




#Password Generator

import random

letters = ["a", "h", "g", "z", "q", "f", "s", "r", "e", "h", "g", "z", "q", "f", "s", "r", "e", "h", "g", "z", "q", "f", "s", "r", "e", "h", "g", "z", "q", "f", "s", "r", "e"]
numbers = ["0", "1", "2", "5", "6", "7", "8", "9", "4", "3", "1", "2", "5", "6", "7", "8", "9", "4", "3", "1", "2", "5", "6", "7", "8", "9", "4", "3"]
symbols = ["!", "@", "#", "$", "%", "^", "<", ">", "{", "}", "@", "#", "$", "%", "^", "<", ">", "{", "}", "@", "#", "$", "%", "^", "<", ">", "{", "}"]

           
print("Welcome to the Password Generator")

letter_input = int(input("How many letters do you want to be in the Password? \n "))
number_input = int(input("How many numbers do you want to be in the Password? \n "))
symbol_input = int(input("How many symbols do you want to be in the Password? \n "))

letter = "".join(random.sample(letters, letter_input))
number = "".join(random.sample(numbers, number_input))
symbol = "".join(random.sample(symbols, symbol_input))

result = letter + number + symbol


randomized = "".join(random.sample(result, len(result)))


print(f"{randomized}")


number = 6

def my_function():
    print("Hello")
    print("World")

for step in range(6):
    my_function()

while number > 0:
    my_function()
    number -=1
    
    import random

word_list = ["aardvark", "baboon", "camel"]

    
words = random.choice(word_list).lower()

display = []

for letter in words:
    display +="_"
    
print(display)

guessed = input("Guess a letter \n")

for position in range(len(words)):
    letter = words[position]
    if letter == guessed:
        display[position] = letter


print(display)


def greetings(name):
    print(f"Wagwan {name}")
    print(f"Yoo{name}")
    print(f"Ekaale {name}")
    
greetings("Jendor")




##Prime number

def prime(num):
    is_prime = True
    for i in range(2,num-1):
        if num % i == 0:
            is_prime = False
    if is_prime:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")


value = int(input("Pick a number from 0-100 \n"))

prime(value)


"""

"""
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n ")

text = input("Type your message: \n").lower()

shift = int(input("Type the shift number: \n"))


def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")

encrypt(text, shift)


#print(alphabet.index("c"))

"""

# print(type(str([1, 2,3])))
# print(str([1, 2,3]) + " Godly")

# b = "Hello, World!"
# print(b[2:4])

# a = "Hello, World"
# print(a.strip())

# thislist = ["apple", "banana", "cherry"]
# thislist.append("damson")


# thistuple = ("apple", "banana", "cherry")
# print(type(thistuple))

# thisset = {"apple", "banana", "cherry", "agb", "weq","sd"}
# print(thisset)

# print("My name is Jide")

# def my_function(name):
#  print(f"{name} Refsnes")

# my_function("Emil")

# print("My name is jide")

"""
n = int(input("Pick a number between 1-21 \n"))
if n > 21:
    print("The value of your Input must be < 21")
else:
    for number in range(0, n):
        squared = number ** 2
        print(squared)

"""

"""""
def is_leap(year):
    leap = False
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False

    return leap


year = int(input("The Digit"))
print(is_leap(year))

"""""

""""
initial = int(input("What's your first number?: "))
print("+\n-\n*\n/")
operator = input("Pick an operation: ")
following = int(input("Whats your next number?: "))

first_answer = ""

if operator == "+":
   first_answer = initial + following
   print(first_answer)
elif operator == "-":
    first_answer = initial - following
    print(first_answer)
elif operator == "*":
    first_answer = initial * following
    print(first_answer)
elif operator == "/":
    first_answer = initial / following
    print(first_answer)
else:
    print("pick one of the signs above")
    
"""

"""
def format_name(f_name, l_name):
    first_name = f_name.title()
    last_name = l_name.title()
    return first_name + " " + last_name

new_string = format_name("john", "YU")

print(new_string)
"""


# from art import logo

def addition(n1, n2):
    return n1 + n2


def subtraction(n1, n2):
    return n1 - n2


def multiplication(n1, n2):
    return n1 * n2


def division(n1, n2):
    return n1 / n2


operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division
}

""""
def calculation():
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation from the above listed: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type y to continue or n to exit  ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculation()


calculation()
"""
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
