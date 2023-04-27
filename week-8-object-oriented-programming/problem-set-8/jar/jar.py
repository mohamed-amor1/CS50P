class Jar:
    def __init__(self, capacity=12):
        # Constructor for the Jar class
        # Initializes the jar's capacity and size
        # Raises an exception if the capacity is not a positive integer
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError("Invalid capacity")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        # Overrides the __str__ method to display the jar's contents as a string of cookies
        return "🍪" * self.size

    def add_cookies(self, n):
        # Adds cookies to the jar
        # Raises an exception if n is not a positive integer
        # Raises an exception if the jar would be over capacity after adding n cookies
        if not isinstance(n, int) or n <= 0:
            raise ValueError("Invalid deposit")
        if self._size + n > self._capacity:
            raise ValueError("Over capacity")
        self._size += n

    def remove_cookies(self, n):
        # Removes cookies from the jar
        # Raises an exception if n is not a positive integer
        # Raises an exception if the jar does not contain enough cookies to remove n cookies
        if not isinstance(n, int) or n <= 0:
            raise ValueError("Invalid withdraw")
        if n > self._size:
            raise ValueError(f"You cannot withdraw more than {self._size} cookies.")
        self._size -= n

    @property
    def capacity(self):
        # Getter for the jar's capacity
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        # Setter for the jar's capacity
        # Raises an exception if the new capacity is not a positive integer
        if not isinstance(value, int) or value < 0:
            raise ValueError("Invalid capacity")
        self._capacity = value

    @property
    def size(self):
        # Getter for the jar's current size
        return self._size


def main():
    # Create a new jar and prompt the user for input to deposit and withdraw cookies
    cookie = Jar()
    cookie.capacity = int(input("Enter jar capacity: "))
    cookie.add_cookies(int(input("Deposit: ")))
    cookie.remove_cookies(int(input("How many cookies to withdraw? ")))
    print(cookie)


if __name__ == "__main__":
    # Call the main function if the script is run as the main program
    main()
