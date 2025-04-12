# class methods - allows operations to the class itself
#               - takes (self) as the 1st parameter, which represents the clss itself

# Instance methods = best for operations on instances of the class

# Static methods = best for utility functions that do not need to access to class data

# Class methods = Best for class-level data or require access to the class itself



class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa


    def get_info(self):
        return f"{self.name} - {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total # of students: {cls.count}"

    @classmethod
    def get_average_gpa(cls):
        return f"Class average: {0 if cls.count == 0 else (cls.total_gpa / cls.count):.2f}"

# std1 = Student("Manusha", 3.2)
# std2 = Student("Nirmal", 3.4)
# std3 = Student("Perera", 3.6)

print(Student.get_count())
print(Student.get_average_gpa())
