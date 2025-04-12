#  @property  - decorator used to define a method as a property (it can be accessed like an attribute)
#               Benefit:    Add additional logic when read, write or delete attributes
#               Gives you getter, setter, deleter methods



class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:.1f}cm"

    @property
    def height(self):
        return f"{self._height:.1f}cm"

    @width.setter
    def width(self, w):
        if w > 0:
            self._width = w
        else:
            print("Width must be grater than 0")

    @height.setter
    def height(self, h):
        if h > 0:
            self._height = h
        else:
            print("Height must be grater than 0")

    @width.deleter
    def width(self):
        del self._width
        print("Width deleted")

    @height.deleter
    def height(self):
        del self._height
        print("Height deleted")

rectangle1 = Rectangle(3,4)

rectangle1.height = 5
rectangle1.width = 7


del rectangle1.height

print(rectangle1.width)
print(rectangle1.height)
