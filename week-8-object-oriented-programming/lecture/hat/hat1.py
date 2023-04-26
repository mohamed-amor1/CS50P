import random  # Import the random module


class Hat:
    # Create a class attribute that contains the possible house names
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    # Create a class method that sorts the name into a random house
    @classmethod
    def sort(cls, name):
        # Use the random.choice() method to randomly select a house from the houses attribute
        # Print a message indicating which house the name was sorted into
        print(f"{name} is in {random.choice(cls.houses)}")


# Call the sort() method on the Hat class and prompt the user to enter a name to be sorted
Hat.sort(input("Name: "))
