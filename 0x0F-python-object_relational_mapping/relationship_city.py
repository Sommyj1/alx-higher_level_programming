#!/usr/bin/python3
""" City class
    """

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base
from sqlalchemy.orm import declarative_base


class City(Base):
    """ City class
    Args:
        Base (Base): Base class
    """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), 

nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
