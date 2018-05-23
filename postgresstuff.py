import psycopg2

connection =psycopg2.connect(dbname="wcoding",user="postgres",password="sw1128");

c= connection.cursor()

c.execute("select * from inventory")

print("select * from inventory;")