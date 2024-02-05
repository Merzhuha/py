def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    numbers = input("Enter a list of numbers separated by spaces: ").split()
    numbers = [int(num) for num in numbers]

    prime_numbers = list(filter(lambda x: is_prime(x), numbers))
    print("Prime numbers:", prime_numbers)

if __name__ == "__main__":
    main()
