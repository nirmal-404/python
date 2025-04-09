
def net_price(list_price, discount=0, tax=2):
    return (list_price * (1 - discount)) * (1 + tax)

price_of_car= net_price(4)
print(f"Price of car = LKR {price_of_car:.2f} M")

price_of_machine = net_price(1, 0.01, 0.18)
print(f"Price of machin = LKR {price_of_machine:.2f} M")


import time

def count(end, start=0):
    for i in range(start, end):
        print(i, end=' ')
        time.sleep(1)
    print(end)
    print("Done")

count(10)
count(10, 5)