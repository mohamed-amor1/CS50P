# re.search(pattern, string, flags)

import re

# Get the email from input and strip any leading or trailing whitespace
email = input("What's your email? ").strip()

# Use regular expression search to check if the email is valid
# This regular expression matches the beginning of the string, followed by one or more word characters (\w+)
# It then matches an optional group consisting of one or more word characters followed by a dot (\w+\.)?
# Next, it matches one or more word characters followed by a dot and one of the specified TLDs
# The regular expression is case-insensitive
if re.search(r"^\w+@(\w+\.)?\w+\.(com|edu|gov|net|org)$", email, re.IGNORECASE):
    # If the regular expression matches, print "Valid"
    print("Valid")
else:
    # If the regular expression doesn't match, print "Invalid"
    print("Invalid")


# '\.edu' : literally ends with '.edu'
# \w : Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
# A|B : either A or B
# (...) : group
# ? : 0 or one occurence
