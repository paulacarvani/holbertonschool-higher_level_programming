#!/usr/bin/python3
"""Module that creates a class Rectangle with
private atribute width and height with his getter and setter
also with conditionals of typeerror and valuerror
Public instance method for calculates area and perimeter
Uses a print() and str() for a string representation
Uses a repr return a string representation of the rectangle
to be able to recreate a new instance by using eval()
prints bye rectangle... when deletes
Public class atribute: number of instances increments and decrease and
print_symbol to print any symbol in the str"""


class Rectangle:
    """Class Rectangle"""
    number_of_instances = 0
    print_symbol = "#"
    """Public class attribute"""

    def __init__(self, width=0, height=0):
        """Privates atributes"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of a rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Calculates the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Prints a string representation"""
        total = ""
        if self.__width != 0 and self.__height != 0:
            total += '\n'.join(str(self.print_symbol) * self.__width
                               for j in range(self.__height))
        return total

    def __repr__(self):
        """Prints with repr"""
        return 'Rectangle(' + str(self.__width) + \
            ', ' + str(self.__height) + ')'

    def __del__(self):
        """Deletes the instance"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
