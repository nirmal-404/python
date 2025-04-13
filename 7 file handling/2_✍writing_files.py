from http.cookies import CookieError

from create_files import file_path

# Plain text
text_data = "I Like Pizza"

file_path = "stuff/output.txt"

try:
    with open(file=file_path, mode="a") as file:
        file.write(text_data + "\n")
        print(f"Text file {file_path} was created")

except FileExistsError:
    print("That file already exists")

# -----------------------------------------------------------

#   list
employees = ["Eugine", "Squidward", "Spongebob", "Patrik"]

file_path = "stuff/employees.txt"

try:
    with open(file=file_path, mode="w") as file:
        for emp in employees:
            file.write(emp + "\n")
        print(f"Text file {file_path} was created")

except FileExistsError:
    print("That file already exists")

# -----------------------------------------------------------

#   Dictionary
import json

employees = {
    "name": "Spongebob",
    "age": 30,
    "job": "Cook"
}

file_path = "stuff/employees.json"

try:
    with open(file=file_path, mode="w") as file:
        json.dump(employees, file, indent=4)
        print(f"JSON file {file_path} was created")

except FileExistsError:
    print("That file already exists")

# -----------------------------------------------------------

# CSV
import csv

employees = [["Name", "Age", "Job"],
             ["Spongebob", 30, "Cook"],
             ["Patrick", 37, "Unemployed"],
             ["Sandy", 27, "Scientist"]]

file_path = "stuff/employees.csv"

try:
    with open(file=file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"CSV file {file_path} was created")

except FileExistsError:
    print("That file already exists")


# -----------------------------------------------------------


# -----------------------------------------------------------
