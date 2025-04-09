my_dctionary = {"A": 1, "B" : 2, "C" : 3}
my_set = {"A", "B", "C"}
my_arr = ["A", "B", "C"]

print("default arr => ", end="")
for letter in my_arr:
    print(letter, end=" ")

print("\nreversed arr => ", end="")
for letter in reversed(my_arr):
    print(letter, end=" ")


print("\ndefault set => ", end="")
for letter in my_set:
    print(letter, end=" ")

# sets cant be reversed
# print("\ndefault set => ", end="")
# for letter in reversed(my_set):
#     print(letter, end=" ")

print("\ndefault dictionary => ", end="")
for el in my_dctionary:
    print(el, end=" ")

print("\reversed dictionary => ", end="")
for el in reversed(my_dctionary):
    print(el, end=" ")


print("\ndefault dictionary keys => ", end="")
for key in my_dctionary.keys():
    print(key, end=" ")

print("\ndefault dictionary values => ", end="")
for value in my_dctionary.values():
    print(value, end=" ")

print("\ndefault dictionary key and values => ")
for key, value in my_dctionary.items():
    print(f"{key} : {value}")