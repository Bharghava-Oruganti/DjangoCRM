import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'admin123'
)

dbCursor =  db.cursor()

# create a database 
dbCursor.execute("CREATE DATABASE django")
print("ALL DONE !")