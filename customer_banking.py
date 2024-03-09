# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
"""
This module provides functionality for creating CD and savings accounts.
"""
from cd_account import create_cd_account
from savings_account import create_savings_account
# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = float(input("Enter the savings account balance: "))
    savings_interest = float(input("Enter the savings account interest rate: "))
    savings_maturity = int(input("Enter the savings account maturity (in months): "))

    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    print("Interest earned on savings account:", interest_earned)
    print("Updated savings account balance:", updated_savings_balance)

    cd_balance = float(input("Enter the CD account balance: "))
    cd_interest = float(input("Enter the CD account interest rate: "))
    cd_maturity = int(input("Enter the CD account maturity (in months): "))
    _, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)
    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print("Interest earned on CD account:", interest_earned)

if __name__ == "__main__":
    # Call the main function
    main()

