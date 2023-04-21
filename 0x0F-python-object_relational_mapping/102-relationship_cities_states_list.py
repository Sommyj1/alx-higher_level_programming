#!/usr/bin/python3
"""A Scripts that prints all City objects from the database hbtn_0e_14_usa
    """

from sys import argv
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, Session


def main():
    # create an engine
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}',
        pool_pre_ping=True)
    # Create all tables in the engine. This is equivalent to "Create Table"
    Base.metadata.create_all(engine)

    try:
        with Session(bind=engine) as session:
            # Query all State objects, and join their cities
            states = session.query(State).order_by(State.id).all()
            for state in states:
                for city in state.cities:
                    print(f"{city.id}: {city.name} -> {state.name}")
    except Exception as e:
        print(f'Something went wrong! {e}')
    finally:
        session.close()


if __name__ == "__main__":

    main()
