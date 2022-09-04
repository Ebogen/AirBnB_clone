#!/usr/bin/python3
"""We defines a class city that inherit from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    This class represents a class that inherits from BaseModel
    the following Public class attributes:
    state_id: string - known as empty string and it will be the state.id
    name: string - stand for empty string
    """

    state_id = ""
    name = ""
