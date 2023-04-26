# classes


class Student:
    def __init__(self, name, house, patronus):
        # Constructor that creates a new Student object with the given name, house, and patronus.
        # It validates the inputs and raises a ValueError if they are invalid or missing.
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        # This method returns a formatted string that describes the student's name and house.
        # It is called when the object is converted to a string (e.g. when printing).
        return f"{self.name} from {self.house}"

    def charm(self):
        # This method matches the student's patronus to a specific value and returns the corresponding emoji.
        # It uses the new match statement introduced in Python 3.10 to replace the traditional switch statement.
        # If the student's patronus doesn't match any of the specified values, it returns the 🦯 emoji (white cane).
        match self.patronus:
            case "Stag":
                return "🦌"
            case "Otter":
                return "🦦"
            case "Jack Russel terrier":
                return "🐶"
            case _:
                return "🦯"


def main():
    # This function prompts the user to enter the student's information and creates a new Student object.
    # It then calls the charm method to determine the student's patronus emoji and prints it to the console.
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm())


def get_student():
    # This function prompts the user to enter the student's name, house, and patronus.
    # It creates a new Student object with the given information and returns it.
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)


if __name__ == "__main__":
    main()
