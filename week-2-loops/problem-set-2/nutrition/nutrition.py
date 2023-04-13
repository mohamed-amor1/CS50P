# Define the dictionary of fruits and their calorie counts
fruits = {
    "apple": "130",
    "avocado": "50",
    "banana": "110",
    "cantaloupe": "50",
    "grapefruit": "60",
    "grapes": "90",
    "honeydew melon": "50",
    "kiwifruit": "90",
    "lemon": "15",
    "lime": "20",
    "nectarine": "60",
    "orange": "80",
    "peach": "60",
    "pear": "100",
    "pineapple": "50",
    "plums": "70",
    "strawberries": "50",
    "sweet cherries": "100",
    "tangerine": "50",
    "watermelon": "80",
}

# Get user input and convert to lowercase
item = input("Item: ").lower()

try:
    # Retrieve the calorie count for the given fruit name(item) using the get() method
    calories = fruits.get(item)

    # Check if calories is not None (i.e., the key was found in the dictionary)
    if calories:
        print("Calories:", calories)
    else:
        # Handle case where the user input was not found in the dictionary
        # If the key (item) does not exist in the dictionary, fruits.get() will return None
        print("Item not found in database.")
except KeyError:
    # Handle any other exceptions that may occur
    print("An error occurred while retrieving the calorie count.")
