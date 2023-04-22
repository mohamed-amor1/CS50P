# create an empty list to hold student data
students = []

# open the 'students.csv' file for reading
with open("students.csv") as file:
    # loop through each line in the file
    for line in file:
        # extract the student's name and house from the line
        name, house = line.rstrip().split(",")

        # create a dictionary to hold the student's data
        student = {"name": name, "house": house}

        # add the student's dictionary to the students list
        students.append(student)


# define a function to get the student's name
def get_name(student):
    return student["name"]


# sort the students list by their name using the get_name function
for student in sorted(students, key=get_name):
    # print the student's name and house
    print(f"{student['name']} is in {student['house']}")
