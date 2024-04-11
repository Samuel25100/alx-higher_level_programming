#!/usr/bin/python3
"""List all states from the database hbtn_0e_0_usa."""
import MySQLdb as mysql
import sys

connection = mysql.connect(
        host='localhost',
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
)
cursor = connection.cursor()
cursor.execute("SELECT * FROM states")
rows = cursor.fetchall()
for row in rows:
    print(row)
cursor.close()
connection.close()
