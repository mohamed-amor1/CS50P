import pyfiglet
import sys
from random import choice

# Get available fonts
available_fonts = pyfiglet.FigletFont.getFonts()

# Check command-line arguments
if len(sys.argv) == 1:
    # No command-line arguments, prompt user for input
    user_input = input("Enter text: ")
    # Choose a random font from the available fonts
    random_font = choice(available_fonts)
    # Generate output with the random font
    result = pyfiglet.figlet_format(user_input, font=random_font)
    # Print output
    print("Output:\n", result)
elif (
    len(sys.argv) == 3
    and (sys.argv[1] == "-f" or sys.argv[1] == "--font")
    and (sys.argv[2] in available_fonts)
):
    # Command-line arguments -f or --font and a valid font name, prompt user for input
    user_input = input("Enter text: ")
    # Generate output with the specified font
    result = pyfiglet.figlet_format(user_input, font=sys.argv[2])
    # Print output
    print("Output:\n", result)
else:
    # Invalid usage, exit with an error message
    sys.exit("Invalid usage. Usage: python <filename.py> [-f/--font] <fontname>")
