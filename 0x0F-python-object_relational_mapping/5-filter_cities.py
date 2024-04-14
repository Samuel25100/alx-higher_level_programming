#!/usr/bin/python3
"""List all states from the database hbtn_0e_0_usa."""
import MySQLdb as mysql
import sys

if __name__ == "__main__":
    connection = mysql.connect(
        host='localhost',
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3],
        port=3306
    )
    cursor = connection.cursor()
    cursor.execute("""SELECT cities.name FROM cities INNER JOIN states
    ON states.id=cities.state_id WHERE states.name=%s
    ORDER BY cities.id ASC""", (sys.argv[4],))
    rows = cursor.fetchall()
    row = list(i[0] for i in rows)
    print(*row, sep=', ')
    cursor.close()
    connection.close()
