import requests

# Set up the search parameters
term_initial = input("Enter artist name: ")

if len(term_initial) > 1:
    term = term_initial.replace(" ", "+")
elif len(term_initial) == 1:
    term = term_initial

entity = "song"
limit = 3

# Make the API request
url = f"https://itunes.apple.com/search?term={term}&entity={entity}&limit={limit}"
response = requests.get(url)

o = response.json()
for result in o["results"]:
    print(result["trackName"])
