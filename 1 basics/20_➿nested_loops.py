rows = 5

# Square - traditional 
for i in range(rows):
    for j in range(rows):
        print("* ", end="")
    print()


print()

# Square - python features 
for i in range(rows):
    print("* " * rows)

# diamond in pyton featues
for i in range(rows):
    print(" " * (rows-i), end="")
    print("* " * i)
for i in range(rows, 0, -1):
    print(" " * (rows-i), end="")
    print("* " * i)

