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

        @property
        def width(self):
            """
            getter for width
            """
            return self.__width

        @width.setter
        def width(self, value):
            """
            setter for width
            """
            if type(value) != int:
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")

            self.__width = value

        @property
        def height(self):
            """
            getter for height
            """
            return self.__height

        @height.setter
        def height(self, value):
            """
            setter for height
            """
            if type(value) != int:
                raise TypeError("height must be an integer")
            if value <= 0:
                raise ValueError("height must be > 0")

            self.__height = value

        @property
        def x(self):
            """
            getter for x
            """
            return self.__x

        @x.setter
        def x(self, value):
            """
            setter for x
            """
            if type(value) != int:
                raise TypeError("x must be an integer")
            if value < 0:
                raise ValueError("x must be >= 0")

            self.__x = value

        @property
        def y(self):
            """
            getter for y
            """
            return self.__y

        @y.setter
        def y(self, value):
            """
            setter for y
            """
            if type(value) != int:
                raise TypeError("y must be an integer")
            if value < 0:
                raise ValueError("y must be >= 0")

            self.__y = value
