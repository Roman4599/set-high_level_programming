#!/usr/bin/python3
"""Script that safely filters states."""

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
        "SELECT * FROM states WHERE name=%s ORDER BY id ASC",
        (state_name,)
    )
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
