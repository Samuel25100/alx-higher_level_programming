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
    cursor.execute("""SELECT GROUP_CONCAT(cities.name SEPARATOR ', ') AS list
    FROM cities INNER JOIN states ON states.id = cities.state_id
    WHERE states.name = %s""", (sys.argv[4],))
    rows = cursor.fetchone()[0]
    print(rows)
    cursor.close()
    connection.close()