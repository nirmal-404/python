# Shape
class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")


# Circle
class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        print(f"It is a circle with an area of {3.14 * self.radius * self.radius}")
        super().describe()


# Square
class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        print(f"It is a square with an area of {self.width * self.width}")
        super().describe()


# Triangle
class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        print(f"It is a triangle with an area of {0.5 * self.width * self.height}")
        super().describe()

circle = Circle(color="red", is_filled=True, radius=5)
square = Square(color="red", is_filled=True, width=5)
triangle = Triangle(color="red", is_filled=True, width=7, height=8)

print(circle.color)
print(circle.is_filled)
print(circle.radius)
print()

print(f"{square.color}")
print(f"{square.is_filled}")
print(f"{square.width}")

print()

print(f"{triangle.color}")
print(f"{triangle.is_filled}")
print(f"{triangle.width}")
print(f"{triangle.height}")

print()

circle.describe()
print()

square.describe()
print()

triangle.describe()
print()