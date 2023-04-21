#!/usr/bin/python3
"""Script that prints state objects and their cities for the name passed
    """

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


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
                print(f'{state.id}: {state.name}')
                for city in state.cities:
                    print(f'\t{city.id}: {city.name}')
    except Exception as e:
        print(f'Something went wrong! {e}')
    finally:
        session.close()


if __name__ == "__main__":

    main()
