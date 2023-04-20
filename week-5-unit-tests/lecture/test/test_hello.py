# This script is located in the 'test' folder and is used to test the entire folder, including any tests inside it.
# You can run the tests using the command 'pytest test', where 'test' is the name of the folder.
# Note that you should execute the command from the parent directory of the 'test' folder.

# Import the 'hello' function from the 'hello' module in the package.
# The package is identified by the presence of the '__init__.py' file in the 'test' folder.
from hello import hello


# Define a test function that checks the output of the 'hello' function with no arguments.
def test_default():
    assert hello() == "hello, world"


# Define a test function that checks the output of the 'hello' function with an argument.
def test_argument():
    assert hello("David") == "hello, David"
