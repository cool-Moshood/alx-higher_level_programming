#!/usr/bin/python3
"""
 a class Rectangle that defines a rectangle
 """


class Rectangle:
    """ Rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initializes the class

        Args:
            width(int, optional): width. Defaulths to 0.
            height (int, optional): height. Defaults to 0.
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    def __repr__(self):
        """Return a string representation of the class

        Return:
            int: height and width
        """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __str__(self):
        """ string representation of class

        Return:
            str: string representation
        """
        x = self.__width
        y = self.height
        new_str = ""

        if x == 0 or y == 0:
            return new_str

        for i in range(y):
            if i == y - 1:
                new_str += str(self.print_symbol) * x
                break
            new_str += str(self.print_symbol) * x + "\n"
        return new_str

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance with width == height == size
        """
        return Rectangle(size, size)

    def __del__(self):
        """print bye Rectangle when deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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
