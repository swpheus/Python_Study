#my_answer=input("what's your favorite color?")

#print(my_answer)

#User_Name= input("Hi what is your name?")

#print("Nice to meet you, "+User_Name+"!")

#User_password=input("user password")
#print("your Password "+User_password+"~")

# My_Number=input("please input a number")
# My_Number=int(My_Number)
# print(My_Number*10)
#User_Name=input("what's your name?")
# User_Age=int(input("How old are you?"))
# User_Fave_Color=input("what's your favorite color?")

# User_Info=[User_Name,User_Age,User_Fave_Color]

# # if User_Age < 18:
#         print("sorry, you can't sign up.")
# # else:
#     print("move to next step.")
#
# if User_Fave_Color.lower()=="blue":
#     print("That's a good color!")
# elif User_Fave_Color.lower()=="red":
#     print("Red is.. okay...")
# else:
#     print("I'm not a fan of that color.")
#
# My_Number=100
#
# if My_Number >5:
#     print("Greater than 5!")
# elif My_Number >10:
#     print("Greater than 10")
# else:
#     print("your number is less than 5")
# if My_Number >5:
#     print("Greater than 10")
# print("Hello!")

# if User_Age >18:
#     if User_Fave_Color.lower() =="blue":
#         print("Blue is cool !")
#         if True:
#             if True:
#                 pass
#     else:
#         print("that's just an color.")
# else:
#     print("sorry, you're too young to sign up!")

#Ask them their order -- pizza or hot dog?
#Tell them the price of their selection (print the price)
#the ask them, if they want to pay by card or cash
#if they want to pay by card, ask them debit or credit
#if they want to pay by cash, tell them no bills over $100

# User_order=input("them their order pizza or hot dog")
# User_Pay=input("what do you want pay card or cash")
# if User_order.lower()=="pizza"and"hot dog":
#     print("pizza 2$ hot dog 3$")
#     if True:
#         User_Pay
#         if User_Pay.lower()=="card":
#             input("debit or credit")
#         elif User_Pay.lower()=="cash":
#             print("no bills over $100")
# else:
#     User_order

# Run_Forever =True
# while Run_Forever:
#     Run_Forever2=True
#     while Run_Forever2:
#         pass
#     Food =input("what's your favorite food")
#     if Food.lower() == 'broccoli':
#         Run_Forever=False
# print("outside of while loop")

#I want an application to run,and ask the user what thier
#name,age and location is.
#after you get all of the information,display
# it back to the user to confirm.
#after you get the user information,do not exit,keep
#running for the next user -- unless someone tells it to exit

# User_Name=input("what's your name? :")
# User_Age=input("How old are you? :")
# User_location=input("where do you live? :")
# User_Info=[User_Name,User_Age,User_location]
# for i in User_Info:
#     print(i)

Run_Forever = True

while Run_Forever:
    User_Name= input("what is your name?")
    User_Age =input("what is your age?")
    User_Location =input("where do you live?")

    correct =input("your name is "+User_Name+
                   ".You are "+User_Age+
                   " and you live in "+User_Location)
    if correct =="y":
        pass
    else:
        Repeat=input("would you like to try again?")
        if Repeat=="exit":
            Run_Forever=False
            print("GoodBye")




