import mysql.connector

i = 1

def insert(name, generic, form, strength, pharmaceuticals, unit_type, unit_price):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="echamber"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO ep_medicine_list (name, generic, form, strength, pharmaceuticals, unit_type, unit_price) VALUES (%s, %s, %s, %s, %s, %s, %s )"
    val = (name, generic, form, strength, pharmaceuticals, unit_type, unit_price)

    mycursor.execute(sql, val)

    mydb.commit()

    global i
    print(f"[{i}] {name} = record inserted.")
    i += 1


def app():
    with open('medx.txt') as f:
        for line in f:
            l = line.split('|')
            s = l[5].split(': ৳')

            if len(s) < 2: 
                ss = 0.0
            else:
                ss = float(s[1].strip().replace("\n",'').replace(",",''))

            insert(l[0].strip(), l[1].strip(), l[2].strip(), l[3].strip(), l[4].strip(), s[0].strip(), ss)

if __name__ == '__main__':
    app()