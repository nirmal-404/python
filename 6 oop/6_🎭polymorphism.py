# POLYMORPHISM => having may forms

# Ways to achieve polymorphism

# 1. Inheritance    ->  an object could be treated of the
# 2. Duck typing    ->  objects must have necessary attributes

from abc  import ABC, abstractmethod

class Shape:
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Pizza(Circle):
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping

shapes = [Circle(4), Square(5), Triangle(6,7), Pizza("Peperoni", 15)]

for shape in shapes:
    print(f"{shape.area()}cm²")