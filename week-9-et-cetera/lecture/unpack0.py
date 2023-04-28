# Define a function to calculate the total value in knuts
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


# Create a list of coin values
coins = [100, 50, 25]

# Call the total function using the values from the coins list
# The * before coins is used to unpack the values in the list
# and pass them as separate arguments to the function
# So total(*coins) is equivalent to calling total(100, 50, 25)
print(total(*coins), "Knuts")
