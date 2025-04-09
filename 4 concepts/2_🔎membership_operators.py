#   in / not in

word= "APPLE"
letter = input("Guess a letter: ")
if letter in word:
    print(f"There is a letter {letter}")
else:
    print(f"{letter} was not found")


# sets
students  = {"Manusha", "Nirmal", "Perera"}
student = input("Guess a name: ")
if student not in students:
    print(f"{student} was not found") 
else:
    print(f"{student} is present")


# dictionary
results={"Manusha" : "A", "Nirmal": "B", "Perera" : "C"}
student = input("Input student name: ")
if student in results:
    print(f"{student}'s grade is {results[student]}")
    
else:
    print(f"{student} not found")


# strings
email = "someone@example.com"
if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")