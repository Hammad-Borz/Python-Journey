class BankAccount:
    """A simple bank account with validated deposit and withdrawal operations."""

    def __init__(self, balance=0):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
        return self.balance


def main():
    account = BankAccount(1000)

    print(f"Initial balance: ${account.balance}")
    print(f"Deposited $500. New balance: ${account.deposit(500)}")
    print(f"Withdrew $300. Current balance: ${account.withdraw(300)}")

    try:
        account.withdraw(2000)
    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()
