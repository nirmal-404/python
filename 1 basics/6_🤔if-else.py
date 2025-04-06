age = int(input("Enter your age: "))

if 0 < age <= 100:
    if age >= 18:
        print("You are an adult")
    elif age >= 5:
        print("You are a preschooler")
    elif age >= 2:
        print("You are a toddler")
    else: 
        print("You are an infant")
else:
    print("Invalid age!")


name = input("Enter your name: ")
name = name.strip()

if name == "":
    print("Name is empty")
else:
    print(f"Hello {name}")
