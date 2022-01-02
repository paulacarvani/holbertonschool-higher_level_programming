#!/usr/bin/python3
"""
script that lists all State objects, and corresponding
City objects, contained in the database hbtn_0e_101_usa
"""

import sqlalchemy
from sys import argv
from sqlalchemy import create_engine
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    row = session.query(State).all()
    for states in row:
        print("{}: {}".format(states.id, states.name))
        for city in states.cities:
            print("    {}: {}".format(city.id, city.name))
    session.close()
