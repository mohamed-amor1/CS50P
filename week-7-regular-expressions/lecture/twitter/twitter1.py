import re

# Get the URL from input and strip any leading or trailing whitespace
url = input("URL: ").strip()

# Use regular expression search to extract the username from the Twitter URL
# This regular expression matches the beginning of the string, followed by "http://" or "https://"
# It then optionally matches "www." before matching "twitter.com/" and capturing the rest of the string (the username)
# The regular expression is case-insensitive
if matches := re.search(
    r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)$", url, re.IGNORECASE
):
    # If the regular expression matches, print the extracted username
    print(f"Username:", matches.group(1))
