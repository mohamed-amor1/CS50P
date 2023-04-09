# This program prompts the user for input and then outputs that same input, replacing each space with ... (i.e., three periods).

prompt = input("type something: ")
prompt = prompt.replace(" ", "...")
print(prompt)
