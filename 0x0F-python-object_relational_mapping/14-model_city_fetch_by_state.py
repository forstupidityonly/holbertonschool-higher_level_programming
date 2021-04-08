#!/usr/bin/python3
"""
    Write a script that lists first State objects from the
    database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
from model_city import City

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(City, State).join(
            State, City.state_id == State.id).order_by(Ciry.id):
        print("{}: ({})".format(instance[1].name,
            instance[0].id, instance[0].name))
    session.close()