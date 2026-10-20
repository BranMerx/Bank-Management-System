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

#Creating actual database
mycur = mycon.cursor()
mycur.execute("CREATE DATABASE IF NOT EXISTS BankDB")
print("Database created successfully")

#Selecting the database and create tables
mycur.execute("USE BankDB")
mycur.execute("""
CREATE TABLE IF NOT EXISTS Customers(
    customer_id INT AUTO_INCREMENT PRIMARY KEY ,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    phone VARCHAR(15),
    address VARCHAR(100)
)
""")

mycur.execute("""
CREATE TABLE IF NOT EXISTS Accounts(
    account_no BIGINT PRIMARY KEY,
    customer_id INT,
    account_type VARCHAR(20),
    balance DECIMAL (10,2),
    FOREIGN KEY(customer_id) REFERENCES Customers(customer_id)
)
""")

mycur.execute("""
CREATE TABLE IF NOT EXISTS BankTransactions(
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    account_no BIGINT,
    transaction_type VARCHAR(20),
    amount DECIMAL(10,2),
    transaction_date DATETIME,
    FOREIGN KEY(account_no) REFERENCES Accounts(account_no)
)
""")

print("Tables created successfully")