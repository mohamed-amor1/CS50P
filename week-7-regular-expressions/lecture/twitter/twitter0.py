import re

# Get the URL from input and strip any leading or trailing whitespace
url = input("URL: ").strip()

# Use regular expression substitution to extract the username from the Twitter URL
# This regular expression matches the beginning of the string, optionally followed by "http://" or "https://"
# It then optionally matches "www." before matching "twitter.com/"
# The rest of the string (the username) is captured in a group and returned
username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)

# Print the extracted username
print(f"Username: {username}")


# ? only applies to the first character before it. in this cas 's'
# unless it's grouped like '(www\.)'
