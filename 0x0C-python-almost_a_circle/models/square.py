#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    """square is special rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """super for all rect inherited vals and decleration for size"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """overide the str function"""
        var = "[Square] ({}) {}/{} - {}"
        return var.format(self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """size getter"""
        return self.height

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update all vals for args or kwargs"""
        var = len(args)
        if len(args) != 0:
            if var > 0:
                self.id = args[0]
            if var > 1:
                self.size = args[1]
            if var > 2:
                self.x = args[2]
            if var > 3:
                self.y = args[3]
        else:
            for itr in kwargs:
                if itr == "id":
                    self.id = kwargs[itr]
                if itr == "size":
                    self.size = kwargs[itr]
                if itr == "x":
                    self.x = kwargs[itr]
                if itr == "y":
                    self.y = kwargs[itr]

    def to_dictionary(self):
        """make object a dict"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
