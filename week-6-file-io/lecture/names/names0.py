# create an empty list to store names
names = []

# prompt user to input their name four times and append each input to the list
for _ in range(4):
    names.append(input("What's your name? "))

# sort the names in alphabetical order and print a personalized greeting for each name
for name in sorted(names):
    # use f-string to insert variable "name" into the greeting message
    print(f"hello, {name}")
