class Student:

    class_year = 2024
    num_of_students = 0
    students_list = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_of_students += 1
        Student.students_list.append(self)

    @classmethod
    def __iter__(cls):
        return iter(cls.students_list)


std0 = Student("Perera", 22)
std1 = Student("Nirmal", 23)
std2 = Student("Manusha", 24)

print(std2.name)
print(std2.age)
print(std2.class_year)

print(f"My graduating class of {Student.class_year} has {Student.num_of_students} student/s")

for student in Student.students_list:
    print(student.name)