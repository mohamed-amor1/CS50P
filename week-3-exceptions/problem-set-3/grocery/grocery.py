grocery = {}

while True:
    try:
        # Prompt the user to enter an item
        item = input("Enter an item (press Ctrl+Z to finish): ").strip().upper()
        if item.isalpha():
            # If the item is already in the grocery dictionary, increment its count
            if item in grocery:
                grocery[item] += 1
            # Otherwise, add the item to the grocery dictionary with a count of 1
            else:
                grocery[item] = 1

    except EOFError:
        # Exit the loop when the user presses Ctrl+D
        print("Your grocery list:")

        # Sort the grocery dictionary by key in ascending order and print the items and their counts
        # The sorted(grocery.items()) function call will return a list of tuples sorted by key in ascending order:
        for key, value in sorted(grocery.items()):
            print(value, key)

        # Exit the program
        break
