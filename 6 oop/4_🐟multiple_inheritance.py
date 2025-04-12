# multiple inheritance  C(A, B)
#multilevel inheritance  C(B) <- B(A) <- A
from colorsys import hsv_to_rgb


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass


rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

rabbit.flee()
fish.flee()

print()

hawk.hunt()
fish.hunt()

print()

rabbit.eat()
fish.eat()
hawk.eat()

print()

rabbit.sleep()
fish.sleep()
hawk.sleep()