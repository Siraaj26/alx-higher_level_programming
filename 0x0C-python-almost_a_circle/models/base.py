#!/usr/bin/python3
"""
Base class for all models
"""

class Base:
    """
    Base class for all models
    """
    def __init__(self, id=None):
        """
        Initializes the class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
