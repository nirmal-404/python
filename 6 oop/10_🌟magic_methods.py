# magic methods = Dunder methods __init__, __str__, __eq__

class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __gt__(self, other):
        return self.num_pages > other.num_pages

    def __lt__(self, other):
        return self.num_pages < other.num_pages

    def __add__(self, other):
        return self.num_pages + other.num_pages

    def __contains__(self, item):
        return item in self.title or item in self.author

    def __getitem__(self, item):
        if item == "title":
            return self.title

        elif item == "author":
            return self.author

        elif item == "num_pages":
            return self.num_pages
        else:
            return  f"Key {item} was not found"

book1 = Book("Ferno the Fire Dragon", "Adam Blade", 128)
book2 = Book("Night of the Living Dummy", "R.L. Stine", 134)
book3 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 223)


print(book1)
print(book2)
print(book3)


print(book1 == book2)
print(book1 > book2)
print(book1 < book2)
print(book1 + book2)

print("Night" in book2)
print("asd" in book2)

print()
print(book1["title"])
print(book1["author"])
print(book1["num_pages"])
print(book1["pizza"])
