# This program calculates the energy (in joules) using the mass-energy equivalence formula E = mc^2,
# where m is the mass in kilograms and c is the speed of light in meters per second squared.

# Get the mass in kilograms from the user
m = int(input("Enter the mass in kilograms: "))

# Set the speed of light in meters per second
c = 300000000

# Square the speed of light using the ** operator
c = c ** 2

# Calculate the energy using the mass-energy equivalence formula
E = m * c

# Print the result using an f-string
print(f"The energy equivalent of {m} kg of mass is {E} joules.")
