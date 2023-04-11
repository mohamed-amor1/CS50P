answer = input(
    "What is the Answer to the Great Question of Life, the Universe, and Everything? ")
valid_answers = {"42", "forty-two", "forty two"}
if answer.lower() in valid_answers:
    print("Yes")
else:
    print("No")


# or
# if answer == "42" or answer == "forty-two" or answer == "forty two":
#     print("Yes")
# else:
#     try:
#         if int(answer) == 42:
#             print("Yes")
#         else:
#             print("No")
#     except ValueError:
#         print("No")
