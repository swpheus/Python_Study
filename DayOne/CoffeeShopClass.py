class Coffee:
   def __init__(self, HotOrIce, Sugar, Cream, Size):
       self.HotOrIce = HotOrIce
       self.Size = Size
       self.Sugar = Sugar
       self.Cream = Cream
       self.Price = 0
       if Size == "L":
           self.Price = 6500
       elif Size == "S":
           self.Price = 5500

class Bagel:
   def __init__(self):
       pass
class Inventory:
   def __init__(self):
       self.InvCounts = {}
       #load from an inventory file
       # ID, Item, Amt
       # 1 Coffee 30
       # 2 Bagel 20
       # 3 Cream 100

   def Add(self, item, amt):
       self.InvCounts[item] += amt
       pass

   def Subtract(self, item, amt):
       pass

   def Save(self):
       pass
       #write the info from the inventory dictionary back to file
