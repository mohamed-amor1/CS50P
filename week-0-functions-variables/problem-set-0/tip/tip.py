def main() -> None:
    dollars = input_to_float("How much was the meal? $")
    percent = input_to_float("What percentage would you like to tip? ")
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def input_to_float(prompt: str) -> float:
    value = input(prompt)
    if '$' in value:
        value = value.replace('$', '')
    if '%' in value:
        value = value.replace('%', '')
        value = float(value) / 100
    else:
        value = float(value)
    return value


if __name__ == '__main__':
    main()
