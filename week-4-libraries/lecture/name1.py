# Import the sys module, which provides access to some variables used or maintained by the interpreter
import sys

# Check the number of command-line arguments
# If there are less than two arguments, print an error message and exit the script with an error code
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

# Print a name tag for each command-line argument passed to the script
# Iterate over a slice of the sys.argv list, starting from the second element (index 1) since the first element(index 0) is the name of the script 'name1.py'
for arg in sys.argv[1:]:
    print("hello, my name is", arg)
