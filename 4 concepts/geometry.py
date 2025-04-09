import math

# Area calculations
def area_circle(radius):
    return math.pi * radius ** 2

def area_rectangle(length, width):
    return length * width

def area_triangle(base, height):
    return 0.5 * base * height

def area_square(side):
    return side ** 2

# Volume calculations
def volume_sphere(radius):
    return (4/3) * math.pi * radius ** 3

def volume_cube(side):
    return side ** 3

def volume_cuboid(length, width, height):
    return length * width * height

def volume_cylinder(radius, height):
    return math.pi * radius ** 2 * height

def volume_cone(radius, height):
    return (1/3) * math.pi * radius ** 2 * height
