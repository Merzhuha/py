def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius

def main():
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"The temperature {fahrenheit}°F is equivalent to {celsius:.2f}°C.")

if __name__ == "__main__":
    main()
