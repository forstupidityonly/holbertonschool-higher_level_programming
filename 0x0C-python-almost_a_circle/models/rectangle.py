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
        """always a good function"""
        return self.width * self.height

    def display(self):
        """visulization"""
        out = (" " * self.x + "#" * self.width) + "\n"
        out *= self.height
        out = "\n" * self.y + out
        print(out, end="")

    def __str__(self):
        """overide the str function"""
        var = "[Rectangle] ({}) {}/{} - {}/{}"
        return var.format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """update all the vals for args and kwargs"""
        var = len(args)
        if len(args) != 0:
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
        else:
            for itr in kwargs:
                if itr == "id":
                    self.id = kwargs[itr]
                if itr == "width":
                    self.width = kwargs[itr]
                if itr == "height":
                    self.height = kwargs[itr]
                if itr == "x":
                    self.x = kwargs[itr]
                if itr == "y":
                    self.y = kwargs[itr]

    def to_dictionary(self):
        """object to dict"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y}
