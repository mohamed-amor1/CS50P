def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    length = len(s)
    if not (2 <= length <= 6):
        return False
    if not s[:2].isalpha():
        return False
    if "0" in s[:-1]:
        return False
    if any(c in s for c in ". !?,"):
        # checks if any of the characters in the string ". !?" are present in the string 's'.
        # The function any() returns True if at least one of the elements in the iterable passed as argument is True.
        return False
    for i in range(length - 1):
        if s[i].isdigit() and s[i + 1].isalpha():
            return False
    return True


main()
