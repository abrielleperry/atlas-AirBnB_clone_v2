#!/usr/bin/python3
""" holds class State"""
import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """Representation of state """
    if models.storage_t == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")


    else:
        @property
        def cities(self):
                """ public getter for cities """
                city_list = []
                all_city = models.storage.all(City)
                for city in all_city.values():
                    if city.state_id == self.id:
                        city_list.append(city)
                return city_list
