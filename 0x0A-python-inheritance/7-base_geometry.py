#!/usr/bin/python3
"""
class BaseGeometry
"""


class BaseGeometry:
    """
    class BaseGeometry
    """
    def __init__(self):
        """
        init method for 'BaseGeometry' class
        """
        pass

    def area(self):
        """
        method to raise 'Exception'
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        method that validates 'value'
        """
        if type(value) not in [int]:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
