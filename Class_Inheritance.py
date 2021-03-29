class Animal:
    def __init__(self):
        self.eyes = 2

    def breathe(self):
        print("Inhale, Exhale.")


class Hustle:
    def __init__(self):
        pass

    @staticmethod
    def hunger():
        print("Always hungry")


class Fish(Animal, Hustle):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        super().hunger()
        # super(Fish, self).breathe()
        # super(Fish, self).hunger()
        print("Doing this underwater")

    @staticmethod
    def swim():
        print("Moving in water")


nemo = Fish()

nemo.breathe()
