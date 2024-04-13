#!/usr/bin/python3
"""Define class State which inherit from Base."""
from sqlalchemy import create_engine, MetaData, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Class define state name and id."""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
