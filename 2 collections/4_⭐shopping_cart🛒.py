
foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q tto quit): ")
    if food.lower() == 'q':
        break
    else:
        price = float(input("Enter the price of a {food}: LKR "))
        foods.append(food)
        prices.append(price)


print("--------------Your cart--------------")

for food in foods:
    print(f"{food}: LKR {prices[foods.index(food)]}")

for price in prices:
    total += price

print(f"Total: LKR {total}")
