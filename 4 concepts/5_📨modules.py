# module = a file containing code you want to include in your program
#        use 'import' to include a module (built-in or your own)
#        useful to break up a large program reusable separate files

# print(help("modules"))
# print(help("math"))

# import math
import math as m
from math import pi
print(m.pi)
print(pi)

a,b,c=1,2,3
print(a,b,c)

import geometry


# Area calculations
print("Area of Circle (radius = 5):", geometry.area_circle(5))
print("Area of Rectangle (length = 10, width = 4):", geometry.area_rectangle(10, 4))
print("Area of Triangle (base = 6, height = 3):", geometry.area_triangle(6, 3))
print("Area of Square (side = 7):", geometry.area_square(7))

print()

# Volume calculations
print("Volume of Sphere (radius = 5):", geometry.volume_sphere(5))
print("Volume of Cube (side = 4):", geometry.volume_cube(4))
print("Volume of Cuboid (length = 8, width = 3, height = 2):", geometry.volume_cuboid(8, 3, 2))
print("Volume of Cylinder (radius = 3, height = 10):", geometry.volume_cylinder(3, 10))
print("Volume of Cone (radius = 3, height = 6):", geometry.volume_cone(3, 6))