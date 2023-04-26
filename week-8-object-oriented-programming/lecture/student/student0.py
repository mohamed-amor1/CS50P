# Tuples
# Once a tuple is created, its values cannot be modified.
# Cannot assign new values to a tuple or modify its existing values
# we can only assign another tuple to a tuple


def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    # ( , ) returns a 'tuple'
    return (name, house)
    # If we want to change values, we return a 'list':
    # return [name, house]


if __name__ == "__main__":
    main()
