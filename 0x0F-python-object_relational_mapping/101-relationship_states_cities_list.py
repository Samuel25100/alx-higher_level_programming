#!/usr/bin/python3
"""Define class State which inherit from Base."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    col = session.query(State)
    for row in col:
        print("{}: {}".format(row.id, row.name))
        for inst in row.cities:
            print("    ", end="")
            print("{}: {}".format(inst.id, inst.name))
