# Open the file "students.csv" in read mode using a "with" statement
with open("students.csv") as file:
    # Iterate over each line in the file
    for line in file:
        # Remove any trailing whitespace (such as a newline) from the line and split it into two parts using the comma as a delimiter
        # The split() method returns a list with two elements, which are assigned to the variables "name" and "house"
        name, house = line.rstrip().split(",")

        # Print the name and house variables using an "f-string" that formats the output
        print(f"{name} is in {house}")
