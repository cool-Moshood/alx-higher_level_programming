#!/usr/bin/python3
"""this module implements the square class"""
from models.rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        """class constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """square size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """square size setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """print square"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)
