#!/usr/bin/python3
"""Defines the common attributes/methods for classes."""
import models
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """A class that shows BaseModel"""
    def __init__(self):
        """Initialize instance attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Update the object's updated_at to the current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

     def to_dict(self):
         """Convert the object into a dictionary"""
         obj_dict = self.__dict__.copy()
         obj_dict['__class__'] = self.__class__.__name__
         obj_dict['created_at'] = self.created_at.isoformat()
         obj_dict['updated_at'] = self.updated_at.isoformat()
         return obj_dict

    def __str__(self):
        """Return the string representation."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
