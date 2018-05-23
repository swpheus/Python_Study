import sqlite3

class CoffeeShop:

    def __init__(self):
        pass

    class Item:
        def __init__(self, row):
            self.ID = row[0]
            self.ItemName = row[1]
            self.ItemPrice = row[2]
            self.QtyRemaining = row[3]

        def __repr__(self):
            return str(self.ID) + " " + self.ItemName


    def loaditemsfromdatabase(self):
        conn = sqlite3.connect('mydatabase')
        c = conn.cursor()
        c.execute('pragma foreign_keys=ON')

        c.execute('SELECT ID, ItemName, ItemPrice, QtyRemaining FROM ItemList')

        itemList = []
        for row in c.fetchall():
            itemList.append(CoffeeShop.Item(row))

        return itemList

    def updateinventory(self, itemList):
        conn = sqlite3.connect('mydatabase')
        c = conn.cursor()
        c.execute('pragma foreign_keys=ON')

        for i in itemList:
            c.execute("UPDATE ItemList SET QtyRemaining = {} WHERE ID = "
                      "{}".format(i.QtyRemaining, i.ID))

        conn.commit()

    def insertorderhistory(self, order_id, current_order):
        conn = sqlite3.connect('mydatabase')
        c = conn.cursor()
        c.execute('pragma foreign_keys=ON')
        for i in current_order:
            c.execute("INSERT INTO OrderHistory (OrderID, ItemID, Qty, Price) VALUES"
                      " ('{}','{}','{}','{}')".format(order_id, i[0], i[1], i[2]))

        conn.commit()



# class Coffee:
#
#     def __init__(self, hotorice, sugar, cream, size):
#         self.ItemName = "Coffee"
#         self.HotOrIce = hotorice
#         self.Size = size
#         self.Sugar = sugar
#         self.Cream = cream
#         self.Price = 0
#         if size == "L":
#             self.Price = 6500
#         elif size == "S":
#             self.Price = 5500
#
#     def __repr__(self):
#         return self.Size + " " + self.ItemName
#
#
# class Bagel:
#
#     def __init__(self, creamcheese, kind):
#         if kind == "Onion":
#             self.ItemName = "OnionBagel"
#         else:
#             self.ItemName = "PlainBagel"
#         self.CreamCheese = creamcheese
#         self.Price = 2000
#
#     def __repr__(self):
#         return self.ItemName


class Inventory:

    def __init__(self):
        Inv_File = open("Inventory.csv", "r")

        self.InvCount = {}
        for line in Inv_File.readlines():
            row = line.split(",")
            self.InvCount[row[0]] = int(row[1])

        Inv_File.close()

    def add(self, item, amt):
        self.InvCount[item] += amt

    def subtract(self, item, amt):
        self.InvCount[item] -= amt

    def save(self):
        Inv_File = open("Inventory.csv", 'w')
        for key, value in self.InvCount.items():
            Inv_File.write("{}, {}\n".format(key, value))

        Inv_File.close()