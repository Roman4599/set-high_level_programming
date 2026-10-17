#!/usr/bin/python3
"""Lists cities by state."""

import sys
import MySQLdb


def main():
    if len(sys.argv) != 4:
        return

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cur = db.cursor()
    cur.execute(
        """SELECT cities.id, cities.name, states.name
           FROM cities
           INNER JOIN states ON cities.state_id = states.id
           ORDER BY cities.id ASC"""
    )
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
