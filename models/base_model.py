#!/usr/bin/python3
"""initiating a base model class"""
import models
import uuid
from datetime import datetime


class BaseModel():
    """
    The basze model class that defines
    all common features\\attributes
    """

    def __init__(self, *args, **kwargs):
        """
        init class that assign attributes to class
        """
        if len(kwargs) > 0:
            for key, values in kwargs.items():
                if key == '__class__':
                    continue
                if key == "created_at" or key == "updated_at":
                    values = datetime.fromisoformat(values)
                setattr(self, key, values)
            return

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        models.storage.new(self)

    def __str__(self):
        """
        a class that returns the string representation
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        updates the class date which saved at
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        function to_dict returns a dictionary with data
        """
        dict = {**self.__dict__}
        dict['__class__'] = type(self).__name__
        dict['created_at'] = dict['created_at'].isoformat()
        dict['updated_at'] = dict['updated_at'].isoformat()

        return dict
