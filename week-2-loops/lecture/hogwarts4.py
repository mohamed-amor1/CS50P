# List '[]' of dictionaries '{}'

students = []
number = int(input("How many students to add? "))
for _ in range(number):
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    student = {"name": name, "house": house, "patronus": patronus}
    students.append(student)

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
