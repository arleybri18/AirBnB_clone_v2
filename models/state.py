#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
    """class state inherith from Base"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete-orphan",
                          backref="state")

    @property
    def cities(self):
        dict_cls = models.storage.all(models.City)
        city_list = []
        for key, value in dict_cls.items():
            if value.state_id == self.id:
                city_list.append(value)
        return city_list
