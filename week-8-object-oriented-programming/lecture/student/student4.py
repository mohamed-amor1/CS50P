class Student:
    def __init__(self, name, house):
        # Constructor that creates a new Student object with the given name and house.
        self.name = name
        self.house = house

    def __str__(self):
        # This method returns a formatted string that describes the student's name and house.
        # It is called when the object is converted to a string (e.g. when printing).
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        # This class method prompts the user to enter the student's name and house.
        # It creates a new Student object with the given information and returns it.
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)


def main():
    # This function prompts the user to enter the student's information and creates a new Student object.
    # It then prints the object to the console using the __str__ method.
    student = Student.get()
    print(student)


if __name__ == "__main__":
    # The main function is called when the script is run.
    main()
