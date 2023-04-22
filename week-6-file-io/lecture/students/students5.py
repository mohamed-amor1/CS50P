import csv

# Create an empty list to store the student information
students = []

# Open the file containing the student information
with open("students.csv") as file:
    # Create a CSV reader object to read the file line by line
    reader = csv.reader(file)

    # For each line in the CSV file, parse the name and home fields and add them to the students list
    for name, home in reader:
        students.append({"name": name, "home": home})

# Sort the students list in alphabetical order by the name field of each student dictionary
# The lambda function specifies the key for sorting by returning the value associated with the key "name".
for student in sorted(students, key=lambda student: student["name"]):
    # Print the name and home fields for each student in the sorted list
    print(f"{student['name']} is from {student['home']}")
