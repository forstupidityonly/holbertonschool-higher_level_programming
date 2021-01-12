#!/usr/bin/python3
"""MY rectangle module"""


class Rectangle:
    """def rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """optional width and height"""
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
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
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """area"""
        return self.__width * self.__height

    def perimeter(self):
        """perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """visual rect"""
        string = ""
        if self.perimeter() > 0:
            for itr in range(self.__height):
                string += (str(self.print_symbol) * self.__width)
                if itr < self.__height - 1:
                    string += '\n'
        return string

    def __repr__(self):
        """reprensentation of rectangle in string format"""
        return 'Rectangle({}, {})'.format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances += -1
    """delete self"""

    def bigger_or_equal(rect_1, rect_2):
        """what rectangle is bigger or equal"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """specific square"""
        return Rectangle(size, size)
