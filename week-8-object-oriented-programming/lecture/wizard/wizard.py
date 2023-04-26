# Define the base class for wizards
class Wizard:
    # Define the constructor method for wizards
    def __init__(self, name):
        # Check if name is missing and raise an error if it is
        if not name:
            raise ValueError("Missing name")
        # Set the name attribute for the wizard object
        self.name = name


# Define a subclass of Wizard for students
class Student(Wizard):
    # Define the constructor method for students
    def __init__(self, name, house):
        # Call the constructor method of the parent class (Wizard) to set the name attribute
        super().__init__(name)
        # Set the house attribute for the student object
        self.house = house


# Define a subclass of Wizard for professors
class Professor(Wizard):
    # Define the constructor method for professors
    def __init__(self, name, subject):
        # Call the constructor method of the parent class (Wizard) to set the name attribute
        super().__init__(name)
        # Set the subject attribute for the professor object
        self.subject = subject


# Create some wizard objects using the classes we defined
wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense Against the Dark Arts")

# Print out some information about the wizard objects we created
print(f"{wizard.name} is a Wizard")
print(f"{student.name} is in {student.house}")
print(f"Professor {professor.name} teaches {professor.subject}")
