def apply_interest(account, interest_function):
    interest_function(account)

calculate_simple_interest = lambda account: account.deposit(account.balance * 0.05)
