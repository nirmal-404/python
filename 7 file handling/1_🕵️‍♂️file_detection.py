import os

file_path = "stuff/test.txt"

if os.path.exists(file_path):
    print(f"The location {file_path} exists")

    if os.path.isfile(file_path):
        print("That is a file")

    elif os.path.isdir(file_path):
        print("That is a directory")
else:
    print(f"That location does not exists")