class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0  # Default area for Shape

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

def main():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    rectangle = Rectangle(length, width)
    print("Area of rectangle:", rectangle.area())

if __name__ == "__main__":
    main()
