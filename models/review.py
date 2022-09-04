#!/usr/bin/python3
"""Defines a class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Represents a class that inherits from BaseModel
    the following Public class attributes:
    place_id: string - represents an empty string: known as Place.id
    user_id: string - represents an empty string: known as User.id
    text: string - represents an empty string
    """

    place_id = ""
    user_id = ""
    text = ""
