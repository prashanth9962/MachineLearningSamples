#!/usr/bin/python
import MySQLdb

# Connect
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="root",
                     db="KissflowStats")

cursor = db.cursor()

# Execute SQL select statement
cursor.execute("SELECT * FROM purchase_order")

for row in cursor.fetchall():
    print row[0],row[1]

# Close the connection
db.close()
