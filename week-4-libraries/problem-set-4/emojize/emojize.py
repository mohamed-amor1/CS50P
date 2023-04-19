import emoji


def main():
    # Prompt user for input
    user_input = input("Please enter some text: ")
    # Generate output with emoji
    output = emoji.emojize(f"Output: {user_input}", language="alias")
    print(output)


if __name__ == "__main__":
    main()
