#!/usr/bin/python3
"""Define class State which inherit from Base."""
from sqlalchemy import create_engine, MetaData, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    col = session.query(State.name, City.id, City.name).filter(
            City.state_id == State.id)
    for row in col:
        print("{}: ({}) {}".format(row[0], row[1], row[2]))
