#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Float, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
import models

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             nullable=False),
                      Column('amenity_id', String(60), ForeignKey
                             ('amenities.id'), nullable=False))


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship("Review", backref="place")
    amenities = relationship("Amenity", secondary=place_amenity,
                             viewonly=False, backref='place_amenities')

    @property
    def reviews(self):
        """getter attribute reviews that returns the list of
        Review instances with place_id equals to the current Place.id"""
        dict_cls = models.storage.all(models.Review)
        review_list = []
        for key, value in dict_cls.items():
            if value.place_id == self.id:
                review_list.append(value)
        return review_list

    @property
    def amenities(self):
        """Getter attribute amenities that returns the list of
        Amenity instances based on the attribute amenity_ids that
        contains all Amenity.id """
        dict_cls = models.storage.all(models.Amenity)
        amenity_list = []
        for key, value in dict_cls.items():
            for iter_id in self.amenity_ids:
                if value.id == iter_id:
                    amenity_list.append(value)
        return amenity_list

    @amenities.setter
    def amenities(self, obj):
        """Setter attribute amenities that handles append method
        for adding an Amenity.id """
        if obj.__name__ == Amenity:
            self.amenity_ids.append(obj.id)
