Project Overview: Banking System

1. Project Structure:
The project is structured as a modular and organized banking system, implemented in Python. It consists of several classes, each handling specific functionalities, and is divided into separate files for maintainability.

2. Classes:
a. Account (account.py)
Represents a basic bank account with deposit, withdrawal, and balance display functionalities.
Validates a 12-digit account number during initialization.
b. SavingsAccount (savings_account.py)
Inherits from Account.
Introduces an interest rate, allowing for interest calculation and addition to the account balance.
c. CreditCardAccount (credit_card_account.py)
Inherits from Account.
Allows users to apply for a credit card, providing credit limit details.
Displays the credit limit and introduces an apply_interest function with a simple interest calculation.
d. EligibilityEvaluator (eligibility_evaluator.py)
Contains functions for collecting applicant information, evaluating eligibility based on predefined criteria, and displaying application results.
e. Utils (utils.py)
Houses utility functions like apply_interest and calculate_simple_interest for common operations.
f. Main (main.py)
Orchestrates the interaction with users, creating instances of accounts, and demonstrating various functionalities.
