#!/usr/bin/python3
"""Create state California with city San Francisco."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


def main():
    if len(sys.argv) != 4:
        return

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, database
        ),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    cali = State(name="California")
    cali.cities.append(City(name="San Francisco"))
    session.add(cali)
    session.commit()

    session.close()


if __name__ == "__main__":
    main()
