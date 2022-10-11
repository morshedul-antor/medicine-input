import mysql.connector

my_db_conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)


mycursor = my_db_conn.cursor()

mycursor.execute("CREATE DATABASE medicinedb")