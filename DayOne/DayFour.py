# My_File=open("OutputFolder/mynewfile2.txt","r",encoding="utf-8")
# #w = write (which erases anything in there)
# #a = append (which writes at the end of the file)
# #r = read (you can't write anything)
#
# # print(type(My_File))
#
# # My_File.write("Hi my name sungwoo!\n")
#
# My_File.write("Hello world \n")
# My_File.write("Hello world2 \n")
# My_File.write("Hello world3 \n")
# My_File.write("Hello world4 \n")
# My_File.write("Hello world5 \n")
#
# # print(My_File.readline())
#
# My_File.close()


# A =3
# print(A==3)
# if A == 3:
#     print("A is 3!!")

# Numbers =[]
# A =0
# while A!= 10:
#     Numbers.append(A)
#     A+=1
# print(Numbers)
#
# for Number in Numbers:
#     print(Number)

#using a for loop, read this file,and put every line in a list
# My_file = open("OutputFolder/mynewfile2.txt","r",encoding="utf-8")
# One_list=[]
# for w in My_file:
#     # print(My_file.readlines())
#     if w[-1]=="\n":
#         One_list.append(w[0:-1])
#     else:
#         One_list.append(w)
# print(One_list)

#Create a university application
#The application should have 4 functions:
#Adding students
#Display students
#Export List of students
#Exit the application

#it should run untill the user exits.

###useful things to remember
#User Input =input("MESSAGE TO DISPlAY")
#if statements
#While loops
#for loops (export will need these depending on how you program)
#open("filename","w/r/a") to "export"
## (essentially,write a file containing the list of students)


def useradding(student_name, studnet_major):
    student_list = [student_name, student_major]
    return


exit=True
while exit==True:
    User_Selection = input("What do you want to do? \n"
                           "1.Adding students,\n"
                           "2.Display students \n"
                           "3.Export List of students \n"
                           "4.Exit the application, select number" )
    if User_Selection=="1":
        student_name = input("your name!")
        student_major = input("your major!")
        useradding(student_name,student_major)

    elif User_Selection=="2":
        print(student_list)
    elif User_Selection=="3":
        MyFile=open("mynewfile2","w",)













