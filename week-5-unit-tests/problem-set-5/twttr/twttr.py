def main():
    text = input("enter text: ")
    text_shorten = shorten(text)
    print(text_shorten)


def shorten(word):
    vowels = ["a", "e", "i", "o", "u"]
    result = ""
    for c in word:
        if c.lower() not in vowels:
            result = result + c
    return result


if __name__ == "__main__":
    main()
