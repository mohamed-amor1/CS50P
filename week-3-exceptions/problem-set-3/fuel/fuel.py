def main():
    fuel = get_fuel("Fraction: ")
    if fuel <= 1:
        print("E")
    elif fuel >= 99:
        print("F")
    else:
        print(f"{fuel}%")


def get_fuel(prompt):
    """Prompts the user for a fuel fraction and returns the percentage."""
    while True:
        try:
            fraction = input(prompt)

            # Split the fraction string into numerator and denominator substrings using the "/" character as the separator.
            # Then, use the map function to convert the substrings to integers and return them as a tuple.
            numerator, denominator = map(int, fraction.split("/"))

            # Check if the numerator is less than or equal to the denominator.
            # If it is, compute the fuel percentage and return it.
            # If not, the fraction is invalid and the loop continues.
            if numerator <= denominator:
                fuel = round((numerator / denominator) * 100)
                return fuel

        except (ValueError, ZeroDivisionError):
            # If an error occurs during input or conversion, continue the loop
            # and prompt the user again.
            pass


if __name__ == "__main__":
    main()
