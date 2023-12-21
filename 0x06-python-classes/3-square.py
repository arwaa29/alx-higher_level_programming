#!/usr/bin/python3

"""square module."""

class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """constructor.
        Args:
            size: length of a side of the square.
        Raises:
            TypeError: If size is not integer
            ValueError: If size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Area of this square.

        Returns:
           the sixe squared.
        """
        return self.__size ** 2
