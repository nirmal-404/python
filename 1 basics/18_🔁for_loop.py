
for i in reversed(range (1, 11)):
    print(i)
print("HAPPY NEW YEAR")


name="Nirmal"
for i in name:
    print(i)


#evens
for i in range(0,101, 2):
    print(i)


# odds
for i in range(1,101, 2):
    print(i)


for i in range(1, 10):
    if i == 3:
        continue
    else:
        if i == 5:
            print(f"breaking when i = {i}")
            break
        else:
            print(i)