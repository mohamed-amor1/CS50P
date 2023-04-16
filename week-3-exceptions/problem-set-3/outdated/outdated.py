# Define a list of month names
MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


# Define a function to format a date as yyyy-mm-dd
def format_date(year, month, day):
    return f"{year}-{str(month).zfill(2)}-{str(day).zfill(2)}"


# Loop indefinitely to prompt the user for a date until a valid date is entered
while True:
    try:
        # Prompt the user for a date
        user_input = input("Enter a date (mm/dd/yyyy or month day, year): ")

        # Check if the date format is mm/dd/yyyy
        if "/" in user_input:
            # Split the date into its components and convert them to integers
            month, day, year = map(int, user_input.split("/"))

            # Check if the month and day are valid
            if 1 <= month <= 12 and 1 <= day <= 31:
                # Format the date as yyyy-mm-dd and print it to the console
                print(format_date(year, month, day))
                # Exit the loop since a valid date was entered
                break

        # Check if the date format is month day, year
        elif "," in user_input:
            # Remove the comma from the date and split it into its components
            user_input = user_input.replace(",", "")
            month, day, year = user_input.split()
            # Convert the day to an integer
            day = int(day)
            if 1 <= day <= 31:
                # Iterate over the list of month names and their corresponding index
                for i, month_name in enumerate(MONTHS):
                    # Check if the month name matches the current month name in the iteration
                    if month == month_name:
                        # Convert the month name to its corresponding number (1-12)
                        month = i + 1
                        # Format the date as yyyy-mm-dd and print it to the console
                        print(format_date(year, month, day))
                        # Exit the loop since a valid date was entered
                        break
                    else:
                        # Raise a ValueError if the month name is invalid
                        raise ValueError("Invalid month name")
            else:
                raise ValueError("Invalid day")

        # Raise a ValueError if the date format is invalid
        else:
            raise ValueError("Invalid date format")

    # Catch and handle any ValueErrors that are raised
    except ValueError as e:
        # Print the error message to the console
        print(f"Error: {e}")
