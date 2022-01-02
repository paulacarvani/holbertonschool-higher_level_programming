#!/usr/bin/python3
"""
7-model_state_fetch_all.py
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def init_sess():
    """initializes session and engine for sqlalchemy DB instance"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    return (engine, session)


def update_state(db):
    """Change the name of the State where id = 2 to New Mexico"""
    session = db[1]
    s = session.query(State).filter(State.id == 2).one()
    s.name = "New Mexico"
    session.add(s)
    session.commit()
    session.close()
    db[0].dispose()


if __name__ == '__main__':
    update_state(init_sess())
