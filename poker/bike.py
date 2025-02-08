import sqlite3
import time
import pandas as pd
# conn = sqlite3.connect('bike.db')
# # Create a cursor object using the cursor() method
# cursor = conn.cursor()

# # Create table
# cursor.execute('''create table mileage (bike_id, mileage, date)''')

class New_bike:

    def __init__(self, brand, model = None, color = None):
        self.brand = brand
        self.model = model
        self.color = color

    def __repr__(self):
        rep = f"Bike('{self.brand}', '{self.model}', '{self.color}')"
        return rep    

    def insert(self):
        try:
            conn = sqlite3.connect('bike.db')
            print("connected...")
            time.sleep(.5)
            cursor = conn.cursor()
            sqlite_insert = """INSERT INTO bikes (brand, model, color) VALUES (?, ?, ?);"""
            data = (self.brand, self.model, self.color)
            cursor.execute(sqlite_insert, data)
            print("inserting record...")
            time.sleep(.5)
            conn.commit()
            print("success!")
        except sqlite3.Error as error:
            print("Failed to insert Python variable into sqlite table:", error)

class Database:
    def __init__(self, name):
        self.conn = sqlite3.connect(name)
        self.cursor = self.conn.cursor()
   
    def get_bikes(self):
        sql = "SELECT * FROM bikes"
        df = pd.DataFrame(self.cursor.execute(sql)   )
        df = df.rename(columns={0: 'Brand', 1: 'Model', 2: 'Color'})
        return df

    def insert_bike(self, brand, model = None, color = None):
        data = (brand, model, color)
        sql = """INSERT INTO bikes (Brand, Model, Color) VALUES (?, ?, ?);"""
        self.cursor.execute(sql, data)
        self.conn.commit()
       

db = Database('bike.db')
db.get_bikes()
db.insert_bike(brand = "Crust", model = "Lightning Bolt", color = "brown")




bike2 = New_bike(brand = 'Crust', model = 'Lightning bolt', color = "brown")
bike2.insert()
print("hi")
