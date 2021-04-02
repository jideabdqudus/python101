def add(*args):
    print(args[1])
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(3,4,5,6,7))


def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)

    n += kwargs["add"]
    n *= kwargs["multiply"]
    return  n

calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kwargs["model"]
        # or use
        self.color = kwargs.get("color")

my_car = Car(make="Nissan", model="GTE", color="red")
print(my_car.color)