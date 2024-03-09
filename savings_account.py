"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account
# Creating a savings Account class that is a subclass of the Account class.
class SavingsAccount(Account):
    def __init__(self, balance, interest):
# Define a function for the Savings Account
        """Creates a savings account, calculates interest earned, and updates the account balance."""
def create_savings_account(balance, interest_rate, months):
    """"
    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        """
    # create an instance of the Account class and pass in the balance and interest parameters.
    # Assuming the Account class is defined elsewhere and imported correctly
    # Create an instance of the Account class, passing in the balance and a default interest rate of 0
    SavingsAccount = Account(balance, 0)

    # Calculate interest earned
    # ADD YOUR CODE HERE
    interest_earned = balance * (interest_rate / 100) * (months / 12) 

    # Update the savings account balance by adding the interest earned
    # ADD YOUR CODE HERE
    updated_balance = balance + interest_earned
    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    SavingsAccount.set_balance(updated_balance) 
    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    SavingsAccount.set_interest(interest_earned)
    # Return the updated balance and interest earned.
    # ADD YOUR CODE HERE
    return updated_balance, interest_earned