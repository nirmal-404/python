menu = {
    "pizza": 960.50,
    "nachos": 1440.50,
    "popcorn": 1920.00,
    "fries": 800.50,
    "chips": 320.00,
    "pretzel": 1120.50,
    "soda": 960.50,
    "lemonade": 1360.00
}

cart = []
total = 0

print("--------------- MENU ---------------")
for key, value in menu.items():
    print(f"{key:10}: lkr {value:.2f}")

print("------------------------------------")

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == 'q':
        break
    elif menu.get(food) is not None:
        cart.append(food)

for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()

print(f"Total: lkr {total:.2f}")