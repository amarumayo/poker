

import sqlite3
import time
import pandas as pd
from datetime import datetime

# conn = sqlite3.connect('budget.db')
# Create a cursor object using the cursor() method
# cursor = conn.cursor()

# # Create table
#cursor.execute('''create table transaction_log (amount, date, comment)''')

# sqlite_insert = """INSERT INTO transaction_log (amount, date, comment) VALUES (1000, "2025-02-01", "open account");"""
# cursor.execute(sqlite_insert)
# print("inserting record...")
# time.sleep(.5)
# conn.commit()

class Database:
    def __init__(self, name):
        self.conn = sqlite3.connect(name)
        self.cursor = self.conn.cursor()
        print(f"Established connection to {name}...")

class Account:
    def __init__(self):
        self.db = Database("budget.db")
        
    def view_transactions(self, start_date = None):
        sql = "SELECT * FROM transaction_log"
        if start_date:
            sql_where = f" WHERE date >= '{start_date}'"
            sql = sql + sql_where
        df = pd.DataFrame(self.db.cursor.execute(sql))
        df = df.rename(columns={0: 'Amount', 1: 'Date', 2: 'Comment'})
        df['Balance'] = df['Amount'].cumsum()
        return df
        
    def debit(
        self, 
        amount,  
        date = datetime.today().strftime('%Y-%m-%d'),
        comment = None):
            self.credit(-amount, date, comment)

    def credit(
        self, 
        amount,  
        date = datetime.today().strftime('%Y-%m-%d'),
        comment = None):
            data = (amount, date, comment)
            sql = """INSERT INTO transaction_log (amount, date, comment) VALUES (?, ?, ?);"""
            if (self.db.cursor.execute(sql, data)):
                self.db.conn.commit()
                print("sucess!")
               
    @property
    def balance(self):
        sql = 'SELECT SUM(amount) FROM transaction_log;'
        df = pd.DataFrame(self.db.cursor.execute(sql))
        return(float(df[0].loc[df.index[0]]))  



chris = Account()
chris.view_transactions(start_date = '2025-02-01')
chris.balance
chris.debit(5000, comment = "testing")
