#  a concise way to create lists in python
#  compact and easier to read than traditional loops
# expressions for value in iterable if condition


doubles = []
for x in range(1, 11):
    doubles.append(x*2)
print(doubles)

doubles = [x * 2 for x in range(1, 11)]
print(doubles)

fruits = ["apple", "grapes", "orange"]
fruits = [fruit.upper() for fruit in fruits]
print(fruits)

nums = [-1, -4, 3, 2, 5, -6, 0]
negative_nums = [num for num in nums if num < 0]
even_nums = [num for num in nums if num % 2 == 0]
print(negative_nums)
print(even_numslll)