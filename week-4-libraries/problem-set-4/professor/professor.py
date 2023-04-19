import random


def main():
    level = get_level()
    print(f"You chose level {level}")
    problems_to_solve = generate_problems(level)
    score = 0
    # Loop through each problem and its answer in the dictionary
    for problem, answer in problems_to_solve.items():
        # Allow up to 3 attempts to answer each problem
        for attempt in range(3):
            try:
                guess = int(input(f"{problem} = "))
                if guess == answer:
                    score += 1
                    break
                else:
                    print("Incorrect answer, try again.")
            except ValueError:
                print("Invalid input, try again.")
        # Print the answer to the problem after 3 failed tries
        if guess != answer:
            print(f"{problem} = {answer}")
    print(f"Your final score is {score} out of {10}.")


def get_level():
    while True:
        try:
            level = int(input("Choose a level (1, 2, or 3): "))
            if level in [1, 2, 3]:
                return level
            else:
                print("Invalid level, please try again.")
        except ValueError:
            print("Invalid input, please try again.")


def generate_problems(level):
    problems = {}
    for i in range(10):
        # Generate random integers based on the selected level
        if level == 1:
            x = random.randint(1, 10)
            y = random.randint(1, 10)
            # Create a new problem string and its answer
            problem = f"{x} + {y}"
            answer = x + y
            # Add the problem and answer to the dictionary
            problems[problem] = answer

        elif level == 2:
            x = random.randint(10, 99)
            y = random.randint(10, 99)
            # Create a new problem string and its answer
            problem = f"{x} + {y}"
            answer = x + y
            # Add the problem and answer to the dictionary
            problems[problem] = answer

        else:  # level == 3
            x = random.randint(100, 999)
            y = random.randint(100, 999)
            # Create a new problem string and its answer
            problem = f"{x} + {y}"
            answer = x + y
            # Add the problem and answer to the dictionary
            problems[problem] = answer

    return problems


if __name__ == "__main__":
    main()
