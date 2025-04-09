# collection = single "variable" used to store multiple values
#     List  = [] ordered and changeable. Duplicates OK


fruits= ["apple", "orange", "banana", "pineapple"]

print(fruits[::-1]) # ['pineapple', 'banana', 'orange', 'apples']
print(fruits[::2]) # ['pineapple', 'orange']


print(dir(fruits))
print(help(fruits))

print(len(fruits))

print("apple" in fruits)
print("pomergranate" in fruits)

fruits[0] = "pears"
fruits.append("grapes")
fruits.remove("pineapple")
fruits.insert(0, "peach")

fruits.sort()
fruits.reverse()

print(fruits.index("apple"))
print(fruits.count("banana"))

fruits.clear()

for fruit in fruits:
    print(fruit)