# Iteration with lists using "len"

students = ["Hermione", "Harry", "Ron", "Luna", "Neville", "Ginny", "Draco"]
for i in range(len(students)):
    print(i + 1, students[i])

    # or
    # print("{} {}".format(i+1, students[i]))
