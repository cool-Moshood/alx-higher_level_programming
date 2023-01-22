#!/usr/bin/python3
"""Base python class module"""


class Base:
    """my base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """base class constuctor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
