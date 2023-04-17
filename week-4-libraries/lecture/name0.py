# Import the sys module, which provides access to some variables used or maintained by the interpreter
import sys

# Print a string and the first command-line argument passed to the script
# sys.argv[0] is the name of the script file('name.py')
# sys.argv[1] is the first command-line argument passed to the script

# Check the number of command-line arguments
# If there are less than two arguments, print an error message and exit the script with an error code
# If there are more than two arguments, print an error message and exit the script with an error code
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

# Print a name tag with the second command-line argument passed to the script
# Convert the name to uppercase using the .upper() method
print("HELLO\nmy name is", sys.argv[1].upper())

# When you run this code with one argument, such as python name.py John, the output will be "hello, my name is John"
# If you run the code without any arguments, you will get an "IndexError: list index out of range" error, because there are no command-line arguments for the script to access.
