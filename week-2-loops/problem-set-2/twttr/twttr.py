text = input("Input: ")
vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
result = ""

# Iterate through each character in the input string
# We don't need to split the text into words and access them individually.
# We can simply iterate through each character in the string.

for c in text:
    # If the character is not a vowel, add it to the result string
    if c not in vowels:
        result += c

# Print the result string
print("Output:", result)
