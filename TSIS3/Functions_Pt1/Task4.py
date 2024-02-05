def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

def main():
    num_list = input("Enter a list of numbers separated by spaces: ").split()
    num_list = list(map(int, num_list))

    prime_numbers = filter_prime(num_list)
    print("Prime numbers:", prime_numbers)

if __name__ == "__main__":
    main()
