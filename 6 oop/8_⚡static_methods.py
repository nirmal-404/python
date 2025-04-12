# Static methods - belongs to the class
#                - Best for utility functions that do not need access to class data



class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions

emp1 = Employee("Manusha", "Manger")
emp2 = Employee("Nirmal", "Cashier")
emp3 = Employee("Perera", "Cook")

print(f"Cook => {Employee.is_valid_position('Cook')}")
print(f"Scientist => {Employee.is_valid_position('Scientist')}")

print()

print(emp1.get_info())
print(emp2.get_info())
print(emp3.get_info())
