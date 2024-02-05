class StringManipulator:
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input("Enter a string: ")

    def printString(self):
        print("Original string:", self.string)
        print("Uppercase string:", self.string.upper())

def main():
    manipulator = StringManipulator()
    manipulator.getString()

    print("\nChoose an option:")
    print("1. Print the original string")
    print("2. Print the string in uppercase")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        manipulator.printString()
    elif choice == '2':
        manipulator.printString()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
