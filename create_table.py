import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="medicinedb"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE medicines (id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, brand_name VARCHAR(255) NOT NULL, generic_name VARCHAR(255) NOT NULL, form VARCHAR(255) NOT NULL, strength VARCHAR(255) NOT NULL, pharmaceutical VARCHAR(255) NOT NULL)")