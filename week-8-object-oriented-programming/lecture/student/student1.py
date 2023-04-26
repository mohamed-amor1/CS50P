# Dictionnaries: we index into dicts using keys or str in general e.g. student["name"]


def main():
    student = get_student()  # get student info from user
    if student["name"] == "Padma":  # check if student's name is "Padma"
        student["house"] = "Ravenclaw"  # if yes, assign "Ravenclaw" to their house
    print(
        f"{student['name']} from {student['house']}"
    )  # print the student's name and house


def get_student():
    name = input("Name: ")  # get student's name from user
    house = input("House: ")  # get student's house from user
    return {
        "name": name,
        "house": house,
    }  # return a dictionary containing the student's name and house


if __name__ == "__main__":
    main()  # call the main function if the script is executed directly
