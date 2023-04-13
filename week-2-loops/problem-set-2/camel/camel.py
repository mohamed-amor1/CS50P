# Convert a given string in camelCase to snake_case.

camelCase = input("camelCase: ")
snake_case = ""
for i in range(len(camelCase)):
    if camelCase[i].isupper():
        snake_case = snake_case + "_" + camelCase[i].lower()
    else:
        snake_case += camelCase[i]
print("snake case:", snake_case)
