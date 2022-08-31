
import mysql.connector
from mysql.connector import errorcode
import datetime

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="rh"
)

mycursor = mydb.cursor()

mycursor.execute("Show tables;")

myresult = mycursor.fetchall()

for x in myresult:
	print(x)
