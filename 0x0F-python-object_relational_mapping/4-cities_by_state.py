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
    cursor.execute("""SELECT cities.id, cities.name,
    states.name FROM cities INNER JOIN states ON states.id=cities.state_id
    ORDER BY cities.id ASC""")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    connection.close()
