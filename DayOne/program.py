from CoffeeShopClasses import Coffee
from CoffeeShopClasses import Bagel
from CoffeeShopClasses import Inventory

Current_Order = []
Exit_Switch = True

def CalculateTotal(Order):
    total = 0
    for item in Order:
        total += item.price

    return total

while Exit_Switch == True:
    Menu_Input = input("1. Input order\n"
                       "2. See inventory\n"
                       "3. Exit\n")

    if Menu_Input == "1":
        Exit_Switch_2 = True

        while Exit_Switch_2 == True:
            Menu_Input_2 = input("1. Coffee\n"
                                 "2. Bagel\n"
                                 "3. Pay order\n"
                                 "4. Main menu\n")

            if Menu_Input_2 == "1":
                # This has to append a coffee to Current_Order
                Menu_Input_Coffee = True

                while Menu_Input_Coffee == True:
                    Coffee_Hot_Cold = input("Hot or ice?\n"
                                            "1. Hot\n"
                                            "2. Cold\n")
                    if Coffee_Hot_Cold == "1":
                        print("You've selected HOT.")
                        Coffee_Hot_Cold = "HOT"
                    elif Coffee_Hot_Cold == "2":
                        print("You've selected COLD.")
                        Coffee_Hot_Cold = "COLD"

                    Coffee_Sugar = input ("Sugar or no?\n"
                                          "1. Sugar\n"
                                          "2. No sugar\n")
                    if Coffee_Sugar == "1":
                        print("You've selected SUGAR.")
                        Coffee_Sugar = 1
                    elif Coffee_Sugar == "2":
                        print("You've selected NO SUGAR.")
                        Coffee_Sugar = 0

                    Coffee_Cream = input("Cream or no?\n"
                                         "1. Cream\n"
                                         "2. No cream\n")
                    if Coffee_Cream == "1":
                        print("You've selected CREAM.")
                        Coffee_Cream = 1
                    elif Coffee_Cream == "2":
                        print("You've selected NO CREAM.")
                        Coffee_Cream = 0

                    Coffee_Size = input("Large or small?\n"
                                        "1. Large\n"
                                        "2. Small\n")
                    if Coffee_Size == "1":
                        print("You've selected LARGE.")
                        Coffee_Size = "LARGE"
                    elif Coffee_Size == "2":
                        print("You've selected SMALL.")
                        Coffee_Size = "SMALL"

                    Coffee_No = input("How many of this same order would you like?\n"
                                      "Please input number.\n")
                    print("You want", Coffee_No, "of these.")

                    Coffee_Order = Coffee(Coffee_Hot_Cold, Coffee_Sugar, Coffee_Cream, Coffee_Size, int(Coffee_No))

                    Current_Order.append(Coffee_Order)

                    Coffee_Continue = input("Would you like to input another coffee order?\n"
                                            "1. Yes\n"
                                            "2. No\n")

                    if Coffee_Continue == "1":
                        pass
                    elif Coffee_Continue == "2":
                        # print("Your coffee order is:\n", Coffee_Order)
                        Menu_Input_Coffee = False

            if Menu_Input_2 == "2":
                # This appends a bagel to Current_Order
                Menu_Input_Bagel = True

                while Menu_Input_Bagel == True:
                    Bagel_Kind = input("Plain or onion?\n"
                                       "1. Plain\n"
                                       "2. Onion\n")
                    if Bagel_Kind == "1":
                        print("You've selected PLAIN.")
                        Bagel_Kind = "PLAIN"
                    elif Bagel_Kind == "2":
                        print("You've selected ONION.")
                        Bagel_Kind = "ONION"

                    Bagel_Cream = input("Cream cheese or no?\n"
                                        "1. Cream cheese\n"
                                        "2. No cream cheese\n")
                    if Bagel_Cream == "1":
                        print("You've selected CREAM.")
                        Bagel_Cream = 1
                    elif Bagel_Cream == "2":
                        print("You've selected NO CREAM.")
                        Bagel_Cream = 0

                    Bagel_No = input("How many of this same order would you like?\n"
                                     "Please input number.\n")
                    print("You want", Bagel_No, "of these.")

                    Bagel_Order = Bagel(Bagel_Kind, Bagel_Cream, int(Bagel_No))

                    Current_Order.append(Bagel_Order)

                    Bagel_Continue = input("Would you like to input another bagel order?\n"
                                           "1. Yes\n"
                                           "2. No\n")

                    if Bagel_Continue == "1":
                        pass
                    elif Bagel_Continue == "2":
                        # print("Your Bagel order is:\n", Bagel_Order)
                        Menu_Input_Bagel = False

            if Menu_Input_2 == "3":

                Current_Invent = Inventory()

                # loop through Current_Order
                for obj in Current_Order: # coffee sugar cream plain onion

                    if hasattr(obj, "hot_or_ice"):
                        Current_Invent.subtract("COFFEE", obj.number)
                        Current_Invent.subtract("CREAM", obj.cream * obj.number)
                        Current_Invent.subtract("SUGAR", obj.sugar * obj.number)

                    else:

                        if hasattr(obj, "plain"):
                            Current_Invent.subtract("PLAIN", obj.plain * obj.number)
                        elif hasattr(obj, "onion"):
                            Current_Invent.subtract("ONION", obj.onion * obj.number)

                        Current_Invent.subtract("CREAM_CHEESE", obj.cream_cheese * obj.number)

                Current_Invent.save()

            if Menu_Input_2 == "4":
                # print("Your current order is:", Current_Order)
                Exit_Switch_2 = False

    if Menu_Input == "2":
        pass

    if Menu_Input == "3":
        Exit_Switch = False



