class Account:

    def __init__(self, account_holder, account_number, balance=0):
        self.account_holder = account_holder
        self.balance = balance

        if self.validate_account_number(account_number):
            self.account_number = account_number
        else:
            raise ValueError("Account number must be exactly 12 digits long.")

    def validate_account_number(self, account_number):
        return len(str(account_number)) == 12

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. Current balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Current balance: ${self.balance}")
        else:
            print("Insufficient funds!")

    def display_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: ${self.balance}")
