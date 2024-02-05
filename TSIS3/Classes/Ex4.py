import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print(f"Coordinates of the point: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)

def main():
    x1 = float(input("Enter x-coordinate of the first point: "))
    y1 = float(input("Enter y-coordinate of the first point: "))
    point1 = Point(x1, y1)

    x2 = float(input("Enter x-coordinate of the second point: "))
    y2 = float(input("Enter y-coordinate of the second point: "))
    point2 = Point(x2, y2)

    point1.show()
    point2.show()

    distance = point1.dist(point2)
    print("Distance between the two points:", distance)

    # Moving point1 to a new position
    new_x = float(input("Enter new x-coordinate for the first point: "))
    new_y = float(input("Enter new y-coordinate for the first point: "))
    point1.move(new_x, new_y)
    point1.show()

if __name__ == "__main__":
    main()
