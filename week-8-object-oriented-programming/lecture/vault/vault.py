# Define a Vault class to represent a collection of wizarding currency
class Vault:
    # Define the constructor method for a Vault object
    def __init__(self, galleons=0, sickles=0, knuts=0):
        # Set the initial amounts of each currency in the vault
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    # Define a string representation for a Vault object
    def __str__(self):
        # Return a string representing the amounts of each currency in the vault
        return f"{self.galleons} Galleons. {self.sickles} Sickles. {self.knuts} Knuts."

    # Define an addition operator for Vault objects
    def __add__(self, other):
        # Add up the amounts of each currency in each vault object
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        # Create a new Vault object with the total amounts of each currency
        return Vault(galleons, sickles, knuts)


# Create some Vault objects to represent the money owned by the Potters and the Weasleys
potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)

# Add the Potters' and Weasleys' money together to get the total amount
total = potter + weasley
print(total)
