#!/usr/bin/python3
"""Filters cities by state name."""

import sys
import MySQLdb


def main():
    if len(sys.argv) != 5:
        return

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cur = db.cursor()
    cur.execute(
        """SELECT cities.name
           FROM cities
           INNER JOIN states ON cities.state_id = states.id
           WHERE states.name = %s
           ORDER BY cities.id ASC""",
        (state_name,)
    )
    rows = cur.fetchall()
    for i, row in enumerate(rows):
        print(row[0], end="")
        if i < len(rows) - 1:
            print(", ", end="")
    print()

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
