#!/usr/bin/python3
"""
module for Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """
    A class representing a rectangle that inherits from the Base class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a Rectangle object with the specified
        width, height, x, y, and optional id.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def area(self):
        """ return the area ofthe rectangle """
        return self.__width * self.__height

    def display(self):
        """print the rectangle with #
        by taking care of x and y """
        print("{}".format("\n" * self.__y), end="")
        for i in range(self.__height):
            print("{}{}".format(" " * self.__x, "#" * self.__width))

    @property
    def width(self):
        """
        Get the width of the rectangle.

        :return: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        :param value: The new width for the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.

        :return: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        :param value: The new height for the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Get the x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Set the x
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Get the y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Set the y
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ Update the class Rectangle """
        count = 0
        for arg in args:
            if count == 0:
                self.id = arg
            if count == 1:
                self.__width = arg
            if count == 2:
                self.__height = arg
            if count == 3:
                self.__x = arg
            if count == 4:
                self.__y = arg
            count += 1
        if count == 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.__width = value
                if key == "height":
                    self.__height = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value

    def to_dictionary(self):
        """returns dictionary represent a Rectangle"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
