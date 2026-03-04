# pymysql is used to connect to a MySQL database and execute SQL queries. 
# It is a pure Python MySQL client library that is compatible with Python 3.
# It is used to connect to a MySQL database, execute SQL queries, and retrieve data from the database.

import pymysql

# Connect to the database
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='password',
    database='mydatabase'
)

try:
    with connection.cursor() as cursor:
        # Execute a SQL query
        sql = "SELECT * FROM users"
        cursor.execute(sql)
        
        # Fetch all the results
        results = cursor.fetchall()
        for row in results:
            print(row)
finally:    connection.close()

