#!/usr/bin/python3
"""Defines the city class
"""
import sys
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from model_state import Base, State


class City(Base):
    """City class linked to the MySQL table cities"""
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
