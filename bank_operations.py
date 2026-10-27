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

mycur = mycon.cursor()


def create_account():
    account_no = int(input("Enter Account Number: " ))
    customer_name = input("Enter Customer Name: ")
    phone = input("Enter Phone Number: ")
    account_type = input("Enter Account Type (Savings/Current): ")
    balance = float(input("Enter Opening Balance: "))

    qry = "SELECT * FROM Accounts WHERE account_no=%s"
    mycur.execute(qry,(account_no))
    result = mycur.fetchone()

    if result is None:
        sql="""
        INSERT INTO ACCOUNTS
        VALUES(%s,%s,%s,%s)
        """

        values=(
            account_no,
            customer_name,
            phone,
            account_type,
            balance
        )

        mycur.execute(sql, values)
        mycon.commit()
        print("\nAccount was created successfully.")
    else:
        print("\nAccount Number already exists.")

def deposit_money():
    acc_no = int(input("Enter Account Number: "))
    qry = "SELECT balance FROM Accounts WHERE account_no=%s"
    mycur.execute(qry, (acc_no,))
    result = mycur.fetchone()

    if result:
        amount = float(input("Enter Deposit Amount: "))

    sql ="""
    UPDATE Accounts
    SET balance = balance + %s
    WHERE account_no = %s
    """

    mycur.execute(sql, (amount, acc_no))
    mycon.commit()

    mycur.execute("""
    INSERT INTO BankTransactions
    (account_no, transaction_type, amount, transaction_date)
    VALUES(%s, %s, %s, NOW())
    """, (acc_no, 'Deposit', amount))

    mycon.commit()

    if result:
        print("\nAmount Deposited Successfully.")
    else:
        print("\nAccount Not Found.")

def withdraw_money():
    acc_no = int(input("Enter Account Number : "))
    qry = "SELECT balance from Accounts WHERE account_no=%s"
    mycur.execute(qry,(acc_no,))
    result = mycur.fetchone()

    if result:
        balance = result[0]
        amount = float(input("Enter withdrawal Amount: "))
        if amount <= balance:
            print("Insufficent Funds.")
            return
    sql = """
    UPDATE Accounts
    SET balance = balance - %s
    WHERE account_no = %s
    """
    mycur.execute(sql, (amount, acc_no))
    mycon.commit()


    mycur.execute("""
    INSERT INTO BankTransactions
    (account_no, transaction_type, amount, transaction_date)
    VALUES (%s, %s, %s, NOW())
    """, (acc_no, 'Withdrawal', amount))

    mycon.commit()

    #Dipalying the result:

    if result:
        if amount <= balance:
            print("Amount withdrawn successfully.")
        else:
            print("Insufficient Funds.")
    else:
        print("Account not found.")