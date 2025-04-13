

file_path = "stuff/test.txt"

try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("That file was not found")

except PermissionError:
    print("You do not have permission to read that file")


#---------------------------------------------------------------------

# JSON
print("--------------------------- JSON ---------------------------")
import json
file_path = "stuff/employees.json"

try:
    with open(file_path, "r") as file:
        content = json.load(file)

        for key, value in content.items():
            print(f"{key} : {value}")

except FileNotFoundError:
    print("That file was not found")

except PermissionError:
    print("You do not have permission to read that dile")






#---------------------------------------------------------------------
# CSV
print("--------------------------- CSV ---------------------------")
import csv
file_path = "stuff/employees.csv"

try:
    with open(file_path, "r") as file:
        content = csv.reader(file)

        for line in content:
            for col in line:
                print(f"{col:10}", end="")
            print()

except FileNotFoundError:
    print("That file was not found")

except PermissionError:
    print("You do not have permission to read that dile")
