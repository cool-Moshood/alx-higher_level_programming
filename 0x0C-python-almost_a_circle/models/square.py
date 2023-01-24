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

    def update(self, *args, **kwargs):
        """update square"""
        count = len(args)
        if count != 0:
            for a in range(count):
                if a == 0:
                    self.id = args[0]
                elif a == 1:
                    self.size = args[1]
                elif a == 2:
                    self.x = args[2]
                elif a == 3:
                    self.y = args[3]

        elif kwargs and len(kwargs) != 0:
            for a, b in kwargs.items():
                setattr(self, a, b)

    def to_dictionary(self):
        """Returns a dict representation of the square"""
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
