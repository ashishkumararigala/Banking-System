from account import Account

class CreditCardAccount(Account):
    def __init__(self, account_holder, account_number, balance=0, credit_limit=0):
        super().__init__(account_holder, account_number, balance)
        self.credit_limit = credit_limit

    def apply_for_credit_card(self):
        print("Credit card application in progress...")
        # Include logic to get credit card details from the user, e.g., credit limit
        self.credit_limit = float(input("Enter desired credit limit for the credit card: "))


    def display_credit_limit(self):
        print(f"Credit Limit: ${self.credit_limit}")

    def apply_interest(account, interest_function):
        interest_function(account)

    calculate_simple_interest = lambda account: account.deposit(account.balance * 0.05)
