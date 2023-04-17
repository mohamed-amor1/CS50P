# Import the cowsay module, which provides a function for printing ASCII art of talking animals
import cowsay

# Import the sys module, which provides access to some variables used or maintained by the interpreter
import sys


# Check the number of command-line arguments
# If there are exactly two arguments, continue with the script
# If there are less or more than two arguments, exit the script with an error message
if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1])
    cowsay.trex("hello, " + sys.argv[1])

else:
    sys.exit("Error: expected exactly one argument")
