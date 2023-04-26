class Student:
    def __init__(self, name, house):
        # Constructor that creates a new Student object with the given name and house.
        self.name = name
        self.house = house

    def __str__(self):
        # This method returns a formatted string that describes the student's name and house.
        # It is called when the object is converted to a string (e.g. when printing).
        return f"{self.name} from {self.house}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    # The @property decorator turns the house method into a read-only property.
    # This allows us to access the house attribute like a regular attribute, but prevents us from modifying it directly.
    @property
    def house(self):
        return self._house

    # The @house setter decorator turns the house method into a property setter.
    # This allows us to set the house attribute using the property syntax, and validates the input before setting the attribute.
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house


def main():
    # This function prompts the user to enter the student's information and creates a new Student object.
    # It then prints the object to the console using the __str__ method.
    student = get_student()
    print(student)


def get_student():
    # This function prompts the user to enter the student's name and house.
    # It creates a new Student object with the given information and returns it.
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    # The main function is called when the script is run.
    main()
