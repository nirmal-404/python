class Car:
    def __init__(self, model, year, color, is_for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.is_for_sale = is_for_sale

    def start(self):
        print(f"The {self.model} starts with a roar.")

    def stop(self):
        print(f"The {self.model} comes to a smooth stop.")

    def honk(self):
        print(f"The {self.model} honks loudly. Beep beep!")

    def apply_brakes(self):
        print(f"The {self.model}'s brakes are applied.")

    def accelerate(self):
        print(f"The {self.model} speeds up quickly.")

    def __str__(self):
        return f"Car Model: {self.model}, Year: {self.year}, Color: {self.color}, For Sale: {'Yes' if self.is_for_sale else 'No'}"
