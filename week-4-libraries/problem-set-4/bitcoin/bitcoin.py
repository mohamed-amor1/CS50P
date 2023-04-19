import sys
import requests

# Define the number of bitcoins to buy and set it to 0 by default
number = 0

# Get the number of bitcoins to buy from command-line argument
if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
else:
    try:
        number = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

try:
    # Make an HTTP GET request to the Coindesk API to get the current Bitcoin price
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

    # Raise an exception if the request was unsuccessful
    response.raise_for_status()

    # Get the USD rate from the response JSON
    data = response.json()
    usd_rate = data["bpi"]["USD"]["rate_float"]

    # Calculate the price of n bitcoins in USD
    price = usd_rate * number

    # Format the price with a thousands separator and four decimal places (formatted_price is a string!!!!)
    formatted_price = format(price, ",.4f")

except (requests.RequestException, KeyError):
    # Handle errors if the request was unsuccessful or the response JSON was invalid
    sys.exit("Error retrieving data")

# Print the price of n bitcoins in USD
print(f"${formatted_price}")
