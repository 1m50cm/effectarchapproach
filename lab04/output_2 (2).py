import math


class Shape:
    def area(self):
        return


class Square(Shape):
    def __init__(self, side):
        self.side = side


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius


def area(shape):
    if isinstance(shape, Circle):
        return math.pi * shape.radius ** 2
    if isinstance(shape, Square):
        return shape.side ** 2


def main():
    square = Square(5)
    print("Area of square:", area(square))

    circle = Circle(3)
    print("Area of circle:", area(circle))


if __name__ == "__main__":
    main()
