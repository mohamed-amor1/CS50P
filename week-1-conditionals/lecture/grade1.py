# Get student score input and validate it
while True:
    try:
        student_score = int(input("Enter student score (0-100): "))
        if 0 <= student_score <= 100:
            break
        else:
            print("Invalid score. Please enter a score between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Determine grade based on student score
if student_score >= 90:
    print("Grade: A")
elif student_score >= 80:
    print("Grade: B")
elif student_score >= 70:
    print("Grade: C")
elif student_score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
