from datetime import date
import re
import inflect

p = inflect.engine()


# Prompts the user for their date of birth in YYYY-MM-DD format and checks if it's valid
def main():
    birth_date = input("Date of Birth (YYYY-MM-DD): ")
    birth_date = check_date_input(birth_date)
    today_date = date.today()
    print(f"Date of Birth: {birth_date}")
    print(f"Current Date: {today_date}")
    birth_date = date.fromisoformat(birth_date)
    minutes = calculate_minutes(birth_date, today_date)
    words = p.number_to_words(minutes)
    print(f"{words} minutes")


# Checks if the date inputted by the user is in YYYY-MM-DD format
def check_date_input(date):
    pattern = r"^[1-2][0-9]{3}-([0][1-9])|([1][0-2])-([0][1-9]|[1-2][0-9]|[3][0-1])$"
    # Using regex to match the pattern of a valid date in the format YYYY-MM-DD
    if matches := re.search(pattern, date):
        return date
    else:
        # If the date is not in the correct format, raise an error and exit the script
        sys.exit(
            "Invalid date format. Please enter your date of birth in YYYY-MM-DD format."
        )


# Calculates the number of minutes between two dates
def calculate_minutes(start_date, end_date):
    difference = end_date - start_date
    # Calculates the total number of seconds and rounds down to the nearest minute
    total_seconds = int(difference.total_seconds())
    minutes = total_seconds // 60
    return minutes


if __name__ == "__main__":
    main()
