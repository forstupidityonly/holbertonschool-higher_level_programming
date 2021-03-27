#!/usr/bin/python3
"""list all states"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    """
        cursor gives ability to have multiple seperate working environments through
        the same connection to the database
    """
cur = db.cursor()
cur.execute("SELECT * FROM states WHERE name = %s ORDER BY states.id ASC",
            (argv[4], ))
rows = cur.fetchall()
for row in rows:
    print (row)
    """
        close all open cursors, and close all open database connections
    """
cur.close()
db.close()
