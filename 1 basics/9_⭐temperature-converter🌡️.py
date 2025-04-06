print("Temperature Converter")
print("1. °C -> °F")
print("2. °F -> °C")

choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    celsius = float(input("Enter temperature (°C): "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{fahrenheit}°F")
elif choice == 2:
    fahrenheit = float(input("Enter temperature (°F): "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{celsius}°C")
else:
    print("Invalid choice. Please select 1 or 2.")