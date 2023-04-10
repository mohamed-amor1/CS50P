# Prompt the user to enter their name
name = input("What's your name? ")

# Match the input name against several cases
match name:
    # If the input name matches "Harry", "Hermione", or "Ron", print "Gryffindor"
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    # If the input name matches "Draco", print "Slytherin"
    case "Draco":
        print("Slytherin")
    # If the input name doesn't match any of the above cases, print "Who?"
    case _:
        print("Who?")
