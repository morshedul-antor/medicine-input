import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="medicines"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE medicine_list (id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL, generic VARCHAR(255) NOT NULL, form VARCHAR(255) NOT NULL, strength VARCHAR(255) NOT NULL, pharmaceuticals VARCHAR(255) NOT NULL, unit_type VARCHAR(255) NOT NULL, unit_price FLOAT NOT NULL)")

print('Table created...')
