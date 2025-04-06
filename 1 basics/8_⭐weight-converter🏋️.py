print("Weight Converter")
print("1. kg -> lbs")
print("2. lbs -> kg")

choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    kg = float(input("Enter weight in kg: "))
    pounds = kg * 2.20462
    print(f"{pounds} lbs")
elif choice == 2:
    pounds = float(input("Enter weight in lbs: "))
    kg = pounds / 2.20462
    print(f"{kg} kg")
else:
    print("Invalid choice. Please select 1 or 2.")
