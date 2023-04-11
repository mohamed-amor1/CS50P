# Get user input and remove commas
greeting = input("Greeting: ")
text = greeting.replace(",", "")

# Split the input into words
words = text.split()

# Check the first word of the input
if words[0].lower() == "hello":
    # If the first word is "hello", print $0
    print("$0")
elif words[0].startswith("h") or words[0].startswith("H"):
    # If the first word starts with "h" or "H", print $20
    print("$20")
else:
    # If none of the above conditions are met, print $100
    print("$100")
