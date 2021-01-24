#!/usr/bin/python3
""" basic getter and setter with no validation"""
from models.base import Base
class Rectangle(Base):
    """bonze rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """init the vals"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """x(spaces before row in rect) getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """y (new lines before rows in rect) getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        return self.width * self.height

    def display(self):
        out = (" " * self.x + "#" * self.width) + "\n"
        out *= self.height
        out = "\n" * self.y + out
        print(out, end="")

    def __str__(self):
        var = "[Rectangle] ({}) {}/{} - {}/{}"
        return var.format(self.id, self.x, self.y, self.width, self.height)
        
    def update(self, *args):
        var = len(args)
        if var > 0:
            self.id = args[0]
        if var > 1:
            self.width = args[1]
        if var > 2:
            self.height = args[2]
        if var > 3:
            self.x = args[3]
        if var > 4:
            self.y = args[4]
