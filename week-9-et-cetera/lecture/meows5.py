# Import the argparse library
import argparse

# Create an ArgumentParser object with a description of the program
parser = argparse.ArgumentParser(description="Meow like a cat")

# Define a command-line argument "-n" that specifies the number of times to meow
# The "default" argument sets the default value to 1
# The "type" argument specifies that the value should be an integer
# The "help" argument provides a description of the argument
parser.add_argument("-n", default=1, help="number of times to meow", type=int)

# Parse the command-line arguments and store them in the "args" variable
args = parser.parse_args()

# Loop "args.n" number of times, where "args.n" is the value of the "-n" command-line argument
for _ in range(args.n):
    # Print the string "meow" for each iteration of the loop
    print("meow")
