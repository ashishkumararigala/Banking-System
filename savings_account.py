from account import Account

class SavingsAccount(Account):
    def __init__(self, account_holder, account_number, balance=0, interest_rate=0.02):
        super().__init__(account_holder, account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Added interest. Current balance: ${self.balance}")
