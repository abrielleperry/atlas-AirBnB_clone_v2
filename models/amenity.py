#!/usr/bin/python
""" holds class Amenity"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Representation of Amenity """
    if models.storage_t == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)

    else:
        @property
        def amenities(self):
            """ public getter for cities """
            amen_list = []
            all_amen = models.storage.all(Amenity)
            for amenity in all_amen.values():
                if amenity == self.id:
                    amen_list.append(amenity)
            return amen_list

