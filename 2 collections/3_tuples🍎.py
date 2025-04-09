# collection = single "variable" used to store multiple values
#     Tuple = () ordered and unchangeable. Duplicates OK. FASTER

fruits= ("apple", "orange", "banana", "pineapple")

# print(dir(fruits))
# print(help(fruits))

print(f"Length: {len(fruits)}")

print("apple" in fruits)
print("pomergranate" in fruits)

print(fruits.count("banana"))


for fruit in fruits:
    print(fruit)