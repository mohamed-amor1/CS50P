names_list = []

# Collect user input and add names to list
while True:
    try:
        user_names = input("Name: ")
        names_list.append(user_names)
    except EOFError:
        break  # Exit loop when the user presses Ctrl+Z

# Print farewell message based on number of names
if len(names_list) == 1:
    print(f"Adieu, adieu, to {names_list[0]}")
elif len(names_list) == 2:
    print(f"Adieu, adieu, to {names_list[0]} and {names_list[1]}")
elif len(names_list) > 2:
    names_list_minus_last = names_list[:-1]
    names_list_last_item = names_list[-1]
    names_string = ", ".join(names_list_minus_last)
    print(f"Adieu, adieu, to {names_string}, and {names_list_last_item}")
