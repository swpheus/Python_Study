# My_Dictionary={ "car":"fast","truck":"big"}
#
# print("car"in My_Dictionary.keys())

# My_String ="Being HEADER text/html sender: bob"\
#         "***** Hi, welcome to python class! ***** 1/1 message END FOOTER"
# Header ="*****"
# My_Start_Index = My_String.find(Header) + len(Header)
# print(My_Start_Index)
# My_End_Index = My_String.rfind("*****")
# My_Real_Message =My_String[My_Start_Index:My_End_Index]
# print(My_Real_Message)

# while True :
#     User_selection = input("what would you like  to do\n"
#                            " .Display student\n"
#                            "3.Export Student List\n"
#                            "4.Exit\n")
#     if User_selection== "1":
#             for student in student_List:
#                 print(student)
#             input("press enter to continue")
#     if User_selection =="2":
#         student_To_Add = input("what is the student's name?")
#         student_List.append(student_To_Add)
#         print("student added")
#     elif User_selection =="3":
#         Out_File = open(Export_File_Location,'w')

## you need to read the file ,load it into your 'program some how'

##once you load it in, provide a user interface,that allows the user to search

#for a word, and display the full article(s) that it is contained In.

#run until a user types the word "EXITPROGRAM"

from collections import OrderedDict
EXITPROGRAM =False
My_File = open('UNDHR.txt', 'r').read()
Counter= 1
Articles ={}
loop =True
while loop :

    while "Article" in My_File:
        start =My_File.find("Article " +str(Counter))
        End =My_File.find("Article " +str(Counter+1))
        Articles[Counter] = My_File[start:End]
        Counter +=1
        My_File= My_File[End:]

    search_a=input("search word Article")

    for v in Articles.values():
        if search_a in v:
            print(v)
        else:
            continue
         # search_a = My_File.find("Article " + str(search_word))
         # My_Dictionary = {search_a: My_File}





