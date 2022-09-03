#!/usr/bin/pyhon3
"""
This represents the base_model for our first full web application: AirBnB clone
"""
import uuid
import models
from datetime import datetime

"""
At this point we define all the common attributes/methods for other classes
"""


class BaseModel:
    """
    We are going to define all attributes
    """

    def __init__(self, *args, **kwargs):
        """we initialize the attributes used
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    f = "%Y-%m-%dT%H:%M:%S.%f"
                    self.__dict__[key] = datetime.strptime(value, f)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        """
        The function returns:
        the class name, id and attribute dictionary of the base_model
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """
            updates the public instance attribute 'updated_at'
            with the current datetime
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
            returns a dictionary containing all keys/values of '__dict__'
            of the instance
        """
        converted = self.__dict__.copy()
        converted["created_at"] = self.created_at.isoformat()
        converted["updated_at"] = self.updated_at.isoformat()
        converted["__class__"] = self.__class__.__name__
        return (converted)
