# dictionary =  a collection of {key:value} pairs
#               ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# print(dir(capitals))
# print(help(capitals))
print(capitals.get("USA"))


if capitals.get("Japan"):
    print("Japan is in the dictionary")
else:
    print("Japan is not in the dictionary")


capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Updated"})
capitals.pop("China")

keys= capitals.keys()
for key in keys:
    print(key)

print()

values= capitals.values()
for value in values:
    print(value)

print()

items = capitals.items()
print(items)

print()
# capitals.clear()

for key, value in capitals.items():
    print(f"{key}: {value}")

print()

print(capitals)