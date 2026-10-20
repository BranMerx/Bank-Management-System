import mysql.connector

#Connection of Python to MySQL
try:
    mycon = mysql.connector.connect(
        host="localhost",
        user = "root",
        password = "Cebolla65@!"
    )

    if mycon.is_connected():
        print("Connected Successfully to MySQL")

except mysql.connector.Error as err:
    print("Error:", err)