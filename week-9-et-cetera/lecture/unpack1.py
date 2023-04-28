# Define a function to calculate the total value in knuts
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


# Create a dictionary of coin values
coins = {"galleons": 100, "sickles": 50, "knuts": 25}

# Call the total function using the values from the coins dictionary
# The ** before coins is used to unpack the values in the dictionary
# and pass them as keyword arguments to the function
# So total(**coins) is equivalent to calling total(galleons=100, sickles=50, knuts=25)
print(total(**coins), "Knuts")
