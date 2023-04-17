# Import the random module, which contains a variety of functions for generating random numbers and values
import random

# Define a list of cards
cards = ["jack", "queen", "king"]

# Call the shuffle() function from the random module to shuffle the order of the cards in the list
random.shuffle(cards)

# Loop through the shuffled list and print out each card
for card in cards:
    print(card)
