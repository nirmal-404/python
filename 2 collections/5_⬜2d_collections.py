
fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "turkey"]

# groceries = [
#     ["apple", "orange", "banana", "coconut"], 
#     ["celery", "carrots", "potatoes"], 
#     ["chicken", "fish", "turkey"]
# ]

# print(groceries)

# print(f"Vegetables: {groceries[1]}")
# print(f"Fav fruit: {groceries[0][0]}")

# for collection in groceries:
#     print(collection)

# for collection in groceries:
#     for item in collection:
#         print(item)
#     print()


#tuples

# groceries = (
#     ("apple", "orange", "banana", "coconut"), 
#     ("celery", "carrots", "potatoes"), 
#     ("chicken", "fish", "turkey")
# )

# print(groceries)

# print(f"Vegetables: {groceries[1]}")
# print(f"Fav fruit: {groceries[0][0]}")

# for collection in groceries:
#     print(collection)

# for collection in groceries:
#     for item in collection:
#         print(item)
#     print()


# sets
groceries = (
    {"apple", "orange", "banana", "coconut"}, 
    {"celery", "carrots", "potatoes"}, 
    {"chicken", "fish", "turkey"}
)

print(groceries)

print(f"Vegetables: {groceries[1]}")


for collection in groceries:
    print(collection)

for collection in groceries:
    for item in collection:
        print(item)
    print()

num_pad = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    ("*", 0, "#")
)

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()