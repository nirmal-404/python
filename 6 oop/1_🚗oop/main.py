from car import Car

car1 = Car("Mustang", 2024, "red", False)

# Print object and its attributes
print(car1)
print("Model:", car1.model)
print("Year:", car1.year)
print("Color:", car1.color)
print("Available:", car1.is_for_sale)

# Invoke all methods
car1.start()
car1.accelerate()
car1.honk()
car1.apply_brakes()
car1.stop()
