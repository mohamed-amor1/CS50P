def main():
    # Prompt user for input and store it in a variable
    user_input = input("What time is it? ")

    # Convert user input to a float value
    time_float = convert_to_float(user_input)

    # Check if the time is within breakfast, lunch, or dinner time range
    if 7 <= time_float <= 8:
        print("breakfast time")
    elif 12 <= time_float <= 13:
        print("lunch time")
    elif 18 <= time_float <= 19:
        print("dinner time")
    else:
        print("Not meal time")


def convert_to_float(time):
    # Check if the time is a.m. or p.m. and remove the suffix
    if time.endswith("a.m.") or time.endswith("A.M."):
        time = time.lower().replace("a.m.", "")
        try:
            # Split hours and minutes and convert them to float values
            hours, minutes = time.split(":")
            hours = float(hours)
            minutes = float(minutes) / 60
            return hours + minutes
        except ValueError:
            # If the input format is invalid, print an error message and exit the program
            print("Invalid input format!")
            exit()
    elif time.endswith("p.m.") or time.endswith("P.M."):
        time = time.lower().replace("p.m.", "")
        try:
            # Split hours and minutes and convert them to float values
            hours, minutes = time.split(":")
            hours = float(hours) + 12
            minutes = float(minutes) / 60
            return hours + minutes
        except ValueError:
            # If the input format is invalid, print an error message and exit the program
            print("Invalid input format!")
            exit()
    else:
        print("Invalid input format!")
        exit()


if __name__ == "__main__":
    main()
