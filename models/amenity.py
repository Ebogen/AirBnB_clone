#!/usr/bin/python3
"""This module defines a class Amenity that inherit frm BaseModel"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """This represents a class that inherits from BaseModel
       Public class attributes:
       name: string - empty string
    """

    name = ""
