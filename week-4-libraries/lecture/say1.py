# Import the cowsay module, which provides a function for printing ASCII art of talking animals
import cowsay
from random import choice

# Import the sys module, which provides access to some variables used or maintained by the interpreter
import sys

# Define a list of available cow characters
cowsay.char_names = [
    "beavis",
    "cheese",
    "cow",
    "daemon",
    "dragon",
    "fox",
    "ghostbusters",
    "kitty",
    "meow",
    "miki",
    "milk",
    "pig",
    "stegosaurus",
    "stimpy",
    "trex",
    "turkey",
    "turtle",
    "tux",
]

# Choose a random cow character from the list
character = choice(cowsay.char_names)

# Check the number of command-line arguments
# If there are exactly two arguments, continue with the script
# If there are less or more than two arguments, exit the script with an error message
if len(sys.argv) == 2:
    # If there are exactly two arguments, print a random character from cowsay greeting the user with the second argument passed to the script

    # Get the function object for the selected cow character
    func = getattr(cowsay, character)

    # Call the function with a greeting and the second command-line argument
    func("hello, " + sys.argv[1])

    # Hard coded way:
    # cowsay.cow("hello, " + sys.argv[1])

else:
    sys.exit("Error: expected exactly one argument")
