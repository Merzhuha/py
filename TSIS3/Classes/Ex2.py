class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0  # Default area for Shape

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length ** 2

def main():
    length = float(input("Enter the length of the square: "))
    square = Square(length)
    print("Area of square:", square.area())

if __name__ == "__main__":
    main()
