#!/usr/bin/python3
"""Script that creates the State “California” with the City “San Francisco”
    """

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    """Main function
    """
    # create an engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2],

                                   argv[3]), pool_pre_ping=True)
    # create all tables in the engine. This is equivalent to "Create Table"
    Base.metadata.create_all(engine)
    # create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # insantiate a Session
    session = Session()
    # create a new State and City objects
    state = State(name="California")
    city = City(name="San Francisco")
    # append the new City object to the State.cities attribute
    state.cities.append(city)
    # add the State object to the session
    session.add(state)
    # add the City object to the session
    session.add(city)
    # commit the session to the database
    session.commit()

    # close the session
    session.close()


if __name__ == "__main__":
    main()
