import validators

# Ask for user input
email = input("What's your email address? ")

# Check if the email address is valid using the validators module
if validators.email(email):
    print("Valid")
else:
    print("Invalid")
