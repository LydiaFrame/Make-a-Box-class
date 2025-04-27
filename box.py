#!/usr/bin/env python3
"""Module with the Box class."""

class Box:
    """Class to manage a box."""
    
    def __init__(self, length=1, width=1, height=1):
        """Constructor to initialize a box with default dimensions."""
        self.length = length
        self.width = width
        self.height = height

    def __str__(self):
        """Return box dimensions as a formatted string."""
        return '{0:.2f} x {1:.2f} x {2:.2f}'.format(self.length, self.width, self.height)

    @property
    def length(self):
        """Getter for length."""
        return self._length

    @length.setter
    def length(self, length):
        """Setter for length."""
        if length > 0:
            self._length = length
        else:
            raise ValueError('Length must be positive')

    @property
    def width(self):
        """Getter for width."""
        return self._width

    @width.setter
    def width(self, width):
        """Setter for width."""
        if width > 0:
            self._width = width
        else:
            raise ValueError('Width must be positive')

    @property
    def height(self):
        """Getter for height."""
        return self._height

    @height.setter
    def height(self, height):
        """Setter for height."""
        if height > 0:
            self._height = height
        else:
            raise ValueError('Height must be positive')

    def calc_surface_area(self):
        """Calculate the surface area of the box."""
        return 2 * (self.length * self.width + self.width * self.height + self.length * self.height)