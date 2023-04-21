def main():
    user_input = input("Fraction: ")
    fuel_percentage_int = convert(user_input)
    gauge_reading = gauge(fuel_percentage_int)
    print(gauge_reading)


def convert(fraction):
    while True:
        try:
            fuel_fraction_str = fraction
            # Split the fraction string into numerator and denominator substrings using the "/" character as the separator.
            # Then, use the map function to convert the substrings to integers and return them as a tuple.
            numerator, denominator = map(int, fuel_fraction_str.split("/"))

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


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
