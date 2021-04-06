
"""
def my_decorator(func):
    def wrap_func():
        print("*******")
        func()
        print("*******")
    return wrap_func

def hello():
    print("Helloooo")


jane = my_decorator(hello)

print(jane())
"""

"""
#Performance
from time import time
def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f"took {t2 - t1} s")
        return result
    return wrapper

@performance
def long_time():
    for i in range(100000):
        i*5

long_time()

"""

"""
# Error Handling
while True:
    try:
        age = int(input("How old are you? "))
        print(age)
    except:
        print("Please enter a number")
    else:
        break
    finally: # Runs regardless
        print("Finally Done")
"""



"""

# Generator Function
def generator_function(num):
    for i in range(num):
        yield i

g = generator_function(10)
print(next(g))
print(next(g))

# for item in generator_function(100):
#     print(item)

"""


"""

my_array = []

def fib(num):
    a = 0
    b = 1
    for item in range(num):
        yield a
        temp = a
        a = b
        b = temp + b

for x in fib(20):
    print(x)

"""


import random


started = True

def guessing_game(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print("You're a genius")
            return True
    else:
        print("Hey Bozo, I said 1-10")
        return False


answer = random.randint(1, 10)

if __name__ == '__main__':
    while started:
        try:
            guess = int(input("Guess a number 1-10: "))
            if guessing_game(guess, answer):
                break
        except ValueError:
            print("Please enter a number")
            continue