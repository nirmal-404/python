# collection = single "variable" used to store multiple values
#     Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates



fruits= {"apple", "orange", "banana", "pineapple"}


print(dir(fruits))
print(help(fruits))

print(f"Length: {len(fruits)}")

print("apple" in fruits)
print("pomergranate" in fruits)

fruits.add("grapes")
fruits.remove("pineapple")

fruits.clear()

for fruit in fruits:
    print(fruit)


new= {1: "apple", 2: "orange", 3: "banana", 4: "pineapple"}
print(new.get(1))