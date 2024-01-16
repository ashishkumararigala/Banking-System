from account import Account
from savings_account import SavingsAccount
from credit_card_account import CreditCardAccount
from eligibility_evaluator import collect_applicant_info, evaluate_eligibility, display_results
from utils import apply_interest, calculate_simple_interest

if __name__ == "__main__":
    account_holder = input("Enter account holder name for basic account: ")
    account_number = input("Enter a 12-digit account number for basic account: ")

    while not len(account_number) == 12 or not account_number.isdigit():
        print("Invalid account number. Please enter a 12-digit number.")
        account_number = input("Enter a 12-digit account number for basic account: ")
    initial_balance = float(input("Enter initial balance for basic account: "))

    basic_account = Account(account_holder=account_holder, account_number=int(account_number), balance=initial_balance)

    deposit_amount = float(input("Enter deposit amount for basic account: "))
    basic_account.deposit(deposit_amount)
    withdraw_amount = float(input("Enter withdrawal amount for basic account: "))
    basic_account.withdraw(withdraw_amount)
    basic_account.display_balance()

    account_holder = input("Enter account holder name for savings account: ")
    account_number = input("Enter a 12-digit account number for savings account: ")

    while not len(account_number) == 12 or not account_number.isdigit():
        print("Invalid account number. Please enter a 12-digit number.")
        account_number = input("Enter a 12-digit account number for savings account: ")

    initial_balance = float(input("Enter initial balance for savings account: "))


    savings_account = SavingsAccount(account_holder=account_holder, account_number=int(account_number),
                                     balance=initial_balance)

    deposit_amount = float(input("Enter deposit amount for savings account: "))
    savings_account.deposit(deposit_amount)
    withdraw_amount = float(input("Enter withdrawal amount for savings account: "))
    savings_account.withdraw(withdraw_amount)
    savings_account.add_interest()
    interest_rate=0.02
    savings_account.display_balance()

    apply_for_credit_card = input("Do you want to apply for a credit card? (yes/no): ").lower()

    if apply_for_credit_card == "yes":
        credit_card_account = CreditCardAccount(account_holder=account_holder,
                                                account_number=int(account_number),
                                                balance=initial_balance)
        credit_card_account.apply_for_credit_card()
        credit_card_account.display_credit_limit()
    else:
        print("No credit card application. Exiting program.")
        exit()
