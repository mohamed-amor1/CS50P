def main() -> None:
    user_input = input(
        "Please enter a sentence containing ':)' or ':(' to replace with emojis: ")
    user_input = convert(user_input)
    print(user_input)


def convert(text: str) -> str:
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text


if __name__ == '__main__':
    main()
