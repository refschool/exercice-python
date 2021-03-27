#pip install mysql-connector-python
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='memory',
                                         user='root',
                                         password='root')



    cursor = connection.cursor()
    cursor.execute("select * from scoretable;")
    record = cursor.fetchall()
    print("You're connected to database: ", record)
except Error as e:
    print("Error while connecting to MySQL", e)
    
#http://dev.mysql.com/downloads/connector/python/