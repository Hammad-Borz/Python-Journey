class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ${amount}")
        print(f"New balance: ${self.balance}")
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: ${amount}")
            print(f"Current Balance: ${self.balance}")
        else:
            print("Insufficient balance!")
account = BankAccount(1000)
account.deposit(500)
account.withdraw(300)
account.withdraw(2000)