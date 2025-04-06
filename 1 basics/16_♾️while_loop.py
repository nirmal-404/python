
name = input("Enter your name: ").strip()

while name == "":
    print("Name cannot be empty. Please enter a valid name.")
    name = input("Enter your name: ").strip()

age = input("Enter your age: ").strip()

while age == "" or int(age)< 0:
    print("Age cannot be negative. Please enter a valid age.")
    age = input("Enter your age: ").strip()

print(f"Hello {name}. You are {int(age)} years old.")