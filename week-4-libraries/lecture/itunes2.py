# Search songs by artist name using iTunes API
import requests

# Get the artist name from the user
artist_name = input("Enter artist name: ")

# Replace spaces with + sign to prepare it for the URL
term = artist_name.replace(" ", "+")

# Send a request to iTunes API to get the list of songs by the artist
search_url = f"https://itunes.apple.com/search?term={term}&entity=song"
search_response = requests.get(search_url)

# Get the response as JSON
search_result = search_response.json()


# Check if the "results" key exists in the JSON response
if "resultCount" in search_result and search_result["resultCount"] > 0:
    # Loop through the list of results and print the artist name and track name for each song
    for song in search_result["results"]:
        if song["artistName"].lower() == artist_name.lower():
            print(f"{song['artistName']} - {song['trackName']}")
else:
    print("No results found.")
