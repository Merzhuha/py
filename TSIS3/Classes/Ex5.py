class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of ${amount} accepted. Current balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of ${amount} accepted. Current balance: ${self.balance}")
        else:
            print("Insufficient funds for withdrawal.")

def main():
    owner = input("Enter account owner's name: ")
    account = BankAccount(owner)
    print(f"Account owner: {account.owner}")

    while True:
        choice = input("Enter 'D' to deposit, 'W' to withdraw, or 'Q' to quit: ").upper()
        if choice == 'Q':
            break
        elif choice == 'D':
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        elif choice == 'W':
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
