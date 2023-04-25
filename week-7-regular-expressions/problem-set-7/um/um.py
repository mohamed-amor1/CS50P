import re
import sys


def main():
    # Get input from user and pass to count function
    print(count(input("Text: ")))


def count(s):
    # Remove leading/trailing whitespace and convert to lowercase
    s = s.strip().lower()

    # Use '\b' in the regular expression to match the word "um" only if it appears as a whole word
    pattern = r"\bum\b"

    # Find all occurrences of pattern in s and store in matches list
    matches = re.findall(pattern, s)

    # Return the number of matches
    return len(matches)


if __name__ == "__main__":
    main()
