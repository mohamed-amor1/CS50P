# Define a class named Account
class Account:
    def __init__(self):
        # Set the initial balance of the account to zero
        self._balance = 0

    # Define a property method that returns the balance of the account
    @property
    def balance(self):
        return self._balance

    # Define a method to deposit money into the account
    def deposit(self, n):
        self._balance += n

    # Define a method to withdraw money from the account
    def withdraw(self, n):
        self._balance -= n


# Define a main function to test the Account class
def main():
    # Create an instance of the Account class
    account = Account()

    # Print the initial balance of the account
    print("Balance:", account.balance)

    # Deposit 100 into the account
    account.deposit(100)

    # Withdraw 50 from the account
    account.withdraw(50)

    # Print the final balance of the account
    print("Balance:", account.balance)


# Call the main function if the script is being run directly
if __name__ == "__main__":
    main()


# Can't assign a value to balance directly because it is a read-only property of the Account class.
# The balance method that is decorated with @property is only used to retrieve the value of the _balance instance variable.
