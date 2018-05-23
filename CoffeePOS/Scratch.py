import sqlite3

conn=sqlite3.connect('mydatabase');
c=conn.cursor();
# c.execute('SELECT * FROM ItemList')
print(c.fetchall())

c.execute('SELECT * FROM orderHistory')
print(c.fetchall())



