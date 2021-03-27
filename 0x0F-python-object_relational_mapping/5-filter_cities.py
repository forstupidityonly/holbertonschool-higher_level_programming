#!/usr/bin/python3
"""list all cities"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT cities.name FROM cities INNER JOIN states
                ON cities.state_id = states.id WHERE states.name='{:s}'
                ORDER BY cities.id ASC""".format(argv[4]))
    rows = cur.fetchall()
    pyStr = ""
    for row in range(len(rows)):
        if row != len(rows) - 1:
            pyStr += rows[row][0] + ", "
        else:
            pyStr += rows[row][0]
    print(pyStr)
    cur.close()
    db.close()
