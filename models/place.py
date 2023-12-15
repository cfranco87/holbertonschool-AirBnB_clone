#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv


place_amenity = Table('place_amenity', Base.metadata,
                     Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
                     Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)
                    )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id =Column(String(60), ForeignKey('cities.id'), nullable=False) 
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False )
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, default=0.0, nullable=False)
    longitude = Column(Float, default=0.0, nullable=False)
    amenity_ids = []
    
    
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review', backref='place',
                               cascade='all, delete-orphan')

        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False)

    if getenv('HBNB_TYPE_STORAGE') == 'fs':
        @property
        def reviews(self):
            review_list = []
            for ob_id, review in models.storage.all(Review).items():
                if self.id == review.place_id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            """Returns all amenities linked to the place
            """
            am_list = []
            for amenity in self.amenity_ids:
                if amenity.id == self.id:
                    am_list.append(amenity)
            return am_list

        @amenities.setter
        def amenitites(self, amen):
            """Adds an Amenity.id to amenity_ids"""
            if type(amen).__name__ == 'Amenity':
                self.amenity_ids.append(amen)
