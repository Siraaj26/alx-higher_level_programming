#!/usr/bin/python3
"""
Unittests for Base Class
"""
from models.base import Base


class Rectangle(Base):
        """
        class Rectangle implements Base
        """

        def __init__(self, width, height, x=0, y=0, id=None):
            """
            Initializes the instance of the class
            Args:
                width: width of the rectangle
                height: height of the rectangle
                x: x coordinate of the rectangle
                y: y coordinate of the rectangle
                id: id of the rectangle
            """
            super().__init__(id)
            self.width = width
            self.height = height
            self.x = x
            self.y = y
