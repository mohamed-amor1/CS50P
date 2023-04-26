import random  # import the random module


# Define a Hat class
class Hat:
    def __init__(self):
        # Initialize the Hat object with a list of houses
        self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    def sort(self, name):
        # Randomly choose a house for the student's name from the list of houses
        print(name, "is in", random.choice(self.houses))


# Create a new Hat object
hat = Hat()

# Call the sort method on the hat object and prompt the user to enter a name
hat.sort(input("Name: "))
