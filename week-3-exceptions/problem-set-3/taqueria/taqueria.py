# A dictionary of menu items and their prices
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}

# An empty list to store user inputs
items = []
total_price = 0.00
item_price = 0.00

# Loop to get user input until they press Ctrl+D
while True:
    try:
        # Get input from the user and add it to the list of items
        item = input("Item: ").title()
        items.append(item)

        # Added this for better output to the user ==> only show total when correct item is inserted.
        item_null = False

        # Check if the item is in the menu
        if item in menu:
            item_price_dict = menu.get(item)
            if item_price_dict is not None:
                item_price = item_price_dict
                total_price += item_price
        else:
            item_null = True

        if item_null == False:
            print(f"Total: ${total_price:.2f}")  # Display the updated total price

    except EOFError:
        # Exit the loop when the user presses Ctrl+D
        print(f"Final Total: ${total_price:.2f}")
        break
