class Shape:
    area = 0

    def calculate_area(self):
        pass



class Circle(Shape):
    def calculate_area(self):
        radius = float(input("Enter the radius of the circle: "))
        self.area = 3.14 * radius * radius


class Rectangle(Shape):
    def calculate_area(self):
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        self.area = length * width


class Triangle(Shape):
    def calculate_area(self):
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        self.area = 0.5 * base * height


def main():
    shape = Triangle()
    shape.calculate_area()
    print(shape.area)

if __name__ == '__main__':
    main()
