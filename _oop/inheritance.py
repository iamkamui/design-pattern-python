class Animal:
    def __init__(self, name, sex, weight, color):
        self.name = name
        self.sex = sex
        self.weight = weight
        self.color = color

    def breath(self):
        print(f"{self.name} breathing")

    def eat(self, food):
        print(f"{self.name} eating {food}")

    def run(self, destination):
        print(f"{self.name} running to {destination}")

    def sleep(self, hours):
        print(f"{self.name} sleeping for {hours} hours")


class Cat(Animal):
    def __init__(self):
        super().__init__()
        self.isNasty = bool

    def meow(self):
        print("meow")


class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.best_friend = "Human"

    def bark(self):
        print("Wouf")
