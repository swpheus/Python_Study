from CoffeePOS.CoffeeShopClass import CoffeeShop as csc
import datetime

ApplicationTools = csc()
ItemList = ApplicationTools.loaditemsfromdatabase()
Current_Order = []



def checkout(Current_Order):
    time=datetime.datetime.now()
    total = 0
    for i in Current_Order:
        total += i[2]

    print("Your total is ", total)
    print("your date",time)
    input("Press enter to continue...")
    ApplicationTools.insertorderhistory(time, Current_Order)

def closeapp():
    ApplicationTools.updateinventory(ItemList)
    exit()

while True:
    print("Select your order")
    for i in ItemList:
        print(i)
    print("100 Check Out")
    print("101 Exit")
    selection = int(input()) - 1

    if selection == 99:
        checkout(Current_Order)
        Current_Order = []
    elif selection == 100:
        closeapp()
    else:
        qty = int(input("How many?"))
        ItemList[selection].QtyRemaining -= qty
        selectedItem = ItemList[selection]

        Current_Order.append([selectedItem.ID, qty, selectedItem.ItemPrice * qty])
