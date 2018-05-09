#Create a POS System
#We only sell Americanos and Bagels
#We want to be able to control inventory
#We want to be able to order multiple items at one time.
#Eventually we will want credit processing, but for now we only take cash
#(please program with this in mind for the future)
#Track the orders -- create a history of orders,
# containing what was order and how much
#
#Create the framework for everything
#create a class for inventory
   #add and subtract, even if not just from an order
#create a class for coffee / bagel (cream, sugar)
   #think about the customization of your items
#create a history for orders -- including the combinations
#keep the system running until user selects exit
#calculate tax rates on final purchase

from CoffeeShopClass import Coffee,Bagel,inventory

Current_Order = []

Current_Order.append(Coffee("Hot", 1, 1, "L"))
Current_Order.append(Coffee("Ice", 2, 2, "S"))
Current_Order.append(Coffee("ice",1,1,"S"))
Current_Order.append(Coffee("Hot",1,2,"L"))
Current_Order.append(Coffee("ice",1,2,"s"))
for order in Current_Order:

 print(order)
# def load(inventory):
#     inventory.Add()
def CalculateTotal(Order):
   total = 0
   for item in Order:
       total += item.Price

   return total

print(CalculateTotal(Current_Order))

