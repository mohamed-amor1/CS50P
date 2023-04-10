# Get user input for number and validate it
while True:
    try:
        user_number = int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Determine if number is even or odd
if user_number % 2 == 0:
    print(f"{user_number} is even")
else:
    print(f"{user_number} is odd")
