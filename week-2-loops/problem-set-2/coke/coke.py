# Define a list of valid coin denominations
valid_coins = [25, 10, 5]

# Set the amount due to 50 and initialize user amount to 0
amount_due = 50
user_amount = 0

# Loop until the full amount due is paid
while amount_due > 0:
    print("Amount Due:", amount_due)

    # Prompt the user to insert a coin and convert the input to an integer
    coin = int(input("Insert Coin: "))

    # Check if the user's coin is valid
    if coin in valid_coins:
        # Add the coin to the user's total amount and subtract from the amount due
        user_amount += coin
        amount_due -= coin
    else:
        # If the user's coin is invalid, prompt them to insert a valid coin
        print("Invalid Coin. Please insert a valid coin.")

# Calculate the change owed to the user
if user_amount > 50:
    change_owed = user_amount - 50
    print("Change Owed:", change_owed)
elif user_amount == 50:
    # If the user has paid the full amount, print a thank you message
    print("Thank you for your purchase!")
else:
    # If the user has not paid the full amount, prompt them to insert more coins
    print("Insufficient funds. Please insert more coins.")
