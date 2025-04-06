principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principal amount: "))
    if principle < 0:
        print("Principal amount can't be less than 0")
    else:
        break

while True:
    rate = float(input("Enter the intrest rate: "))
    if principle < 0:
        print("Intrest rate can't be less than 0")
    else:
        break

while True:
    time = int(input("Enter the time in years: "))
    if principle < 0:
        print("Time can't be less than 0")
    else:
        break

total = principle * pow((1+rate / 100), time)

print(f"Balance after {time} year/s under {rate}% compound intrest: {total:.2f}")