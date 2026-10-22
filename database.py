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

#Verifying the tables and close connection
mycur.execute("SHOW TABLES")
print("Tables in BankDB:")
for table in mycur.fetchall():
    print(table[0])

#Inserting Sample Data
mycur.execute("""
INSERT INTO Customers (first_name, last_name, phone, address)
VALUES
('John', 'Smith', '1234567890', 'New York'),
('Emma', 'Johnson', '2345678901', 'Chicago'),
('Michael', 'Brown', '3456789012', 'Los Angeles')
""")

mycur.execute("""
INSERT INTO Accounts (account_no, customer_id, account_type, balance)
VALUES
(10001, 1, 'Savings', 5000.00),
(10002, 2, 'Current', 12000.00),
(10003, 3, 'Savings', 8000.00)
""")

mycur.execute("""
INSERT INTO BankTransactions
(account_no, transaction_type, amount, transaction_date)
VALUES
(10001, 'Deposit', 5000.00, NOW()),
(10002, 'Deposit', 12000.00, NOW()),
(10003, 'Deposit', 8000.00, NOW())
""")

mycon.commit()

print("Sample Data Inserted Successfully")

#Verifying the inserted data
mycur.execute("SELECT * FROM Customers")

print("Customers:")

for row in mycur.fetchall():
    print(row)

mycur.execute("SELECT * FROM Accounts")

print("\nAccounts:")

for row in mycur.fetchall():
    print(row)

mycur.execute("SELECT * FROM BankTransactions")

print("\nBank Transactions:")

for row in mycur.fetchall():
    print(row)
