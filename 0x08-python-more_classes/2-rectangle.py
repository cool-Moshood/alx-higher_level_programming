#!/usr/bin/python3
"""
 a class Rectangle that defines a rectangle
 """


class Rectangle:
    """ Rectangle class"""
    def __init__(self, width=0, height=0):
        """initializes the class

        Args:
            width(int, optional): width. Defaulths to 0.
            height (int, optional): height. Defaults to 0.
        """
        self.height = height
        self.width = width

    def area(self):
        """calculate an area of a Rectangle

        Return:
            int: area
        """
        return self.height * self.width

    def perimeter(self):
        """calculate a perimeter of a Rectangle

        Return:
            int: perimeter
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (2 * self.height) + (2 * self.width)

    @property
    def width(self):
        """width getter

        Return:
            int: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """width setter

        Args:
            value (int): new width

        Raises:
            ValueError: width must be >= 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter

        Return:
            int: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height setter

        Args:
            value (int): height

        Raises:
            ValueError: height must be >= 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
