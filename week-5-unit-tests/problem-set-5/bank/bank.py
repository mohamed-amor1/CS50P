def main():
    # Get user input and remove commas
    user_input = input("Greeting: ")
    greeting_value = value(user_input)
    print(greeting_value)


def value(greeting):
    greeting = greeting.replace(",", "")

    # Split the input into words
    words = greeting.split()

    # Check the first word of the input
    if words[0].lower() == "hello":
        # If the first word is "hello", return $0
        return "$0"
    elif words[0].startswith("h") or words[0].startswith("H"):
        # If the first word starts with "h" or "H", return $20
        return "$20"
    else:
        # If none of the above conditions are met, return $100
        return "$100"


if __name__ == "__main__":
    main()
