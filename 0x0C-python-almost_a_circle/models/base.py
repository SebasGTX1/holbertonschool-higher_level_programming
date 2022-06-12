#!/usr/bin/python3
""" 1. base class """
import json


class Base():
    """ Base class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ constructor method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ public method that returns the JSON representation of
            a list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return []
        return json.dumps(list_dictionaries)
