#!/usr/bin/python3
"""6. Coordinates of a square:
    Write a class Square that defines a square by: (based on 5-square.py)"""


class Square:
    """ Class that defines a Square with size"""
    def __init__(self, size=0, position=(0, 0)):
        """ Method that defines and initialize the size
        of the square

        Args:
            param1 (int): size of the square
            param2 (tuple): position of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """size getter
        Return:
            size value
        """
        return self.__size

    @size.setter
    def size(self, value):
        """size setter

        Args:
            value (int): size
        """
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        """position getter
        Return:
            position value
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ position setter

            Args:
                valie (tuple): position
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Method calculates the area of the square

        Args:
            None
        Return:
            the square's area
        """
        return self.__size * self.__size

    def my_print(self):
        """ Method that prints the square"""
        if self.__size == 0:
            print()
        else:
            for j in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end="")
                for i in range(self.__size):
                    print("#", end="")
                print()
