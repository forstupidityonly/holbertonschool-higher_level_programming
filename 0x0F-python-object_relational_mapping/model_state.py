#!/usr/bin/python3
"""[python files need docstrings and i think length is checked]
    """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """[python files need docstrings and i think length is checked]

    Args:
        Base ([type]): [description]
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
