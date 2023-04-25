import re
import sys


def main():
    user_input = input("Hours: ")
    result = convert(user_input)
    print(result)


def convert(s):
    # Strip leading/trailing whitespace from the input string.
    s = s.strip()
    new_time = ""
    # Define the regular expression pattern to match a time range.
    pattern = r"^([0-9]|1[0-2])(:[0-5][0-9])? (AM|PM) to ([0-9]|1[0-2])(:[0-5][0-9])? (AM|PM)$"

    # Use re.search to search for the pattern in the input string.
    if time := (re.search(pattern, s)):
        if ":" in s:
            hour_1 = int(time.group(1))
            min_1 = time.group(2)
            meridium_1 = time.group(3)
            hour_2 = int(time.group(4))
            min_2 = time.group(5)
            meridium_2 = time.group(6)
            if meridium_1 == "AM" and meridium_2 == "PM":
                if hour_1 == 12 and hour_2 != 12:
                    new_time = f"00{min_1} to {hour_2+12}:{min_2}"
                elif hour_2 == 12 and hour_1 != 12:
                    new_time = f"{hour_1}{min_1} to 00{min_2}"
                elif hour_2 == 12 and hour_1 == 12:
                    new_time = f"00{min_1} to 00{min_2}"
                elif hour_1 < 10 and hour_2 < 10:
                    new_time = f"0{hour_1}{min_1} to {hour_2+12}{min_2}"
                elif hour_1 >= 10 and hour_2 >= 10:
                    new_time = f"{hour_1}{min_1} to {hour_2+12}{min_2}"
                elif hour_1 >= 10 and hour_2 < 10:
                    new_time = f"{hour_1}{min_1} to {hour_2+12}{min_2}"
                elif hour_1 < 10 and hour_2 >= 10:
                    new_time = f"0{hour_1}{min_1} to {hour_2+12}{min_2}"
                # Add a leading 0 to single-digit hours.
                return new_time
            elif meridium_1 == "PM" and meridium_2 == "AM":
                if hour_1 == 12 and hour_2 != 12:
                    new_time = f"00{min_1} to {hour_2}{min_2}"
                elif hour_2 == 12 and hour_1 != 12:
                    new_time = f"{hour_1}{min_1} to 00{min_2}"
                elif hour_2 == 12 and hour_1 == 12:
                    new_time = f"00{min_1} to 00{min_2}"
                elif hour_1 < 10 and hour_2 < 10:
                    new_time = f"{hour_1+12}{min_1} to 0{hour_2}{min_2}"
                elif hour_1 >= 10 and hour_2 >= 10:
                    new_time = f"{hour_1+12}{min_1} to {hour_2}{min_2}"
                elif hour_1 >= 10 and hour_2 < 10:
                    new_time = f"{hour_1+12}{min_1} to 0{hour_2}{min_2}"
                elif hour_1 < 10 and hour_2 >= 10:
                    new_time = f"0{hour_1+12}{min_1} to {hour_2}{min_2}"
                # Add a leading 0 to single-digit hours.
                return new_time
        elif ":" not in s:
            hour_1 = int(time.group(1))
            meridium_1 = time.group(3)
            hour_2 = int(time.group(4))
            meridium_2 = time.group(6)
            if meridium_1 == "AM" and meridium_2 == "PM":
                if hour_1 == 12 and hour_2 != 12:
                    new_time = f"00:00 to {hour_2+12}:00"
                elif hour_2 == 12 and hour_1 != 12:
                    new_time = f"{hour_1}:00 to 00:00"
                elif hour_2 == 12 and hour_1 == 12:
                    new_time = f"00:00 to 00:00"
                elif hour_1 < 10 and hour_2 < 10:
                    new_time = f"0{hour_1}:00 to {hour_2+12}:00"
                elif hour_1 >= 10 and hour_2 >= 10:
                    new_time = f"{hour_1}:00 to {hour_2+12}:00"
                elif hour_1 >= 10 and hour_2 < 10:
                    new_time = f"{hour_1}:00 to {hour_2+12}:00"
                elif hour_1 < 10 and hour_2 >= 10:
                    new_time = f"0{hour_1}:00 to {hour_2+12}:00"
                # Add a leading 0 to single-digit hours.
                return new_time
            elif meridium_1 == "PM" and meridium_2 == "AM":
                if hour_1 == 12 and hour_2 != 12:
                    new_time = f"00:00 to {hour_2}:00"
                elif hour_2 == 12 and hour_1 != 12:
                    new_time = f"{hour_1+12}:00 to 00:00"
                elif hour_2 == 12 and hour_1 == 12:
                    new_time = f"00:00 to 00:00"
                elif hour_1 < 10 and hour_2 < 10:
                    new_time = f"{hour_1+12}:00 to 0{hour_2}:00"
                elif hour_1 >= 10 and hour_2 >= 10:
                    new_time = f"{hour_1+12}:00 to {hour_2}:00"
                elif hour_1 >= 10 and hour_2 < 10:
                    new_time = f"{hour_1+12}:00 to 0{hour_2}:00"
                elif hour_1 < 10 and hour_2 >= 10:
                    new_time = f"{hour_1+12}:00 to {hour_2}:00"
                # Add a leading 0 to single-digit hours.
                return new_time

    else:
        raise ValueError


if __name__ == "__main__":
    main()
