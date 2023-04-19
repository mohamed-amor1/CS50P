import random

# Prompt user for input until a valid integer greater than 0 is entered
while True:
    try:
        n = int(input("Level: "))
        if n > 0:
            break
    except ValueError:
        pass

# Generate a random integer between 1 and n (inclusive)
number = random.randint(1, n)

# Prompt user for input until they correctly guess the number
while True:
    try:
        guess = int(input("Guess: "))
        if guess > 0:
            if guess < number:
                print("Too small!")
            elif guess > number:
                print("Too large!")
            else:
                print("Just right!")
                break
    except ValueError:
        pass
