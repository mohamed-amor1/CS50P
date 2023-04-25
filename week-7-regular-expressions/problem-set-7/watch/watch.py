import re
import sys


def main():
    # Prompt the user for input and print the result of parsing it.
    print(parse(input("HTML: ")))


def parse(s):
    # Remove leading/trailing whitespace from the input string.
    s = s.strip()

    # Define the regular expression pattern to match a YouTube video URL.
    pattern = r"https?://(?:www.)?youtube.com/embed/([a-z0-9_]+)"

    # Use re.search to search for the pattern in the input string, ignoring case.
    if link := re.search(pattern, s, re.IGNORECASE):
        # If a match is found, return the URL of the corresponding video.
        return f"https://youtu.be/{link.group(1)}"
    else:
        # If no match is found, return "None".
        return "None"


if __name__ == "__main__":
    # Call the main function when the script is run.
    main()
