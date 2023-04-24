import re

# Get the name from input and strip any leading or trailing whitespace
name = input("What's your name? ").strip()

# Use regular expression search to check if the name matches the pattern "last, first"
# This regular expression matches the beginning of the string, followed by one or more of any character (except a newline) captured in group 1
# It then matches zero or more spaces followed by a comma and zero or more spaces
# Finally, it matches one or more of any character (except a newline) captured in group 2
if matches := re.search(r"^(.+), *(.+)$", name):
    # If the regular expression matches, re-arrange the name to "first last"
    name = matches.group(2) + " " + matches.group(1)

# Print a personalized greeting
print(f"Hello, {name}!")


# := known as the walrus operator in Python. It is used to assign values to variables within an expression.
# .group(1) starts from 1 not 0
