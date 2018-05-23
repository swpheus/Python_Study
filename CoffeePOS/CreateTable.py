import sqlite3
conn = sqlite3.connect('mydatabase')
c = conn.cursor()
c.execute('pragma foreign_keys=ON')
# c.execute('DROP TABLE ItemList')
# c.execute('DROP TABLE OrderHistory')
c.execute('CREATE TABLE ItemList (ID Integer primary key autoincrement, '
          'ItemName text, ItemPrice real, QtyRemaining integer)')
c.execute('CREATE TABLE OrderHistory (ID Integer primary key autoincrement, '
          'OrderID text, ItemID integer, Qty integer, Price real, foreign key(ItemID) REFERENCES ItemList(ID))')
c.execute('INSERT INTO ItemList (ItemName, ItemPrice, QtyRemaining) VALUES'
          '("Coffee", 4500, 100)')
c.execute('INSERT INTO ItemList (ItemName, ItemPrice, QtyRemaining) VALUES'
          '("Onion Bagel", 3500, 100)')
c.execute('INSERT INTO ItemList (ItemName, ItemPrice, QtyRemaining) VALUES'
          '("Plain Bagel", 3000, 100)')
c.execute('INSERT INTO ItemList (ItemName, ItemPrice, QtyRemaining) VALUES'
          '("Cream Cheese", 100, 100)')
c.execute('INSERT INTO ItemList (ItemName, ItemPrice, QtyRemaining) VALUES'
          '("Salad", 5000, 100)')
c.execute('INSERT INTO ItemList (ItemName, ItemPrice, QtyRemaining) VALUES'
          '("Banana Juice", 2500, 100)')
c.execute('INSERT INTO ItemList (ItemName, ItemPrice, QtyRemaining) VALUES'
          '("Grape Juice", 2500, 100)')
c.execute('SELECT * FROM ItemList')
print(c.fetchall())
c.execute('SELECT * FROM OrderHistory')
print(c.fetchall())
conn.commit()