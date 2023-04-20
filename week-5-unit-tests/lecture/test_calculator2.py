# Import the 'square' function from the 'calculator' module.
from calculator import square

# Import the 'pytest' module, which provides tools for testing Python code.
import pytest


# Define a test function that checks the output of the 'square' function with positive input values.
def test_positive():
    assert square(2) == 4
    assert square(3) == 9


# Define a test function that checks the output of the 'square' function with negative input values.
def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9


# Define a test function that checks the output of the 'square' function with input value of 0.
def test_zero():
    assert square(0) == 0


# Define a test function that checks that the 'square' function raises a TypeError when passed a string argument.
def test_str():
    with pytest.raises(TypeError):
        square("cat")


# This code can be executed in the terminal using the command 'pytest test_calculator1.py'.
# This command will run all the test functions defined in this script and report any failures or errors.
