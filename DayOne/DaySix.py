# total =0
# print(total)
#
# def name():
#     total =3
#     print("Gave")
#     print(total)
# print("nice to meet you!")
# name()
#
# def person(name,age):
#     print(name,age)
#
# person("sung",22)
#
# print("this")

# def addition(First_Number,Second_Number):
#             Third_Number= First_Number+Second_Number
#             print(Third_Number)
#             return
# Name = "gabe"
# Upper_Name =Name.upper()
#
# my_output =addition(3,3)
#
# # m=input("your g transelate kg")
# def trans(m):
#     kg= m*2.2
#
#     return kg
# print(trans(int(input("your g transelate kg"))))


def conversion(pounds):
        kilograms =pounds*2.2

        return kilograms

# print(conversion(100))
# x=conversion(100)
# print(x)

# def conversion(weight,unit):
#     if unit=="Kg":
#         return weight*2.2
#     elif unit=="LB":
#         return weight/2.2
#     else:
#         return
#
# My_output =conversion(100,"Kg")
# print(My_output)
# print(type(My_output))


#F =kelvin * 9/5- 459.67
#F = C*9/5 +32

#kelvin =C - 273.15
#kelvin = (F + 459.67) * 5/9

#C =kelvin + 273.15
#C =(F + 32) * 5/9

def TempConversion(measurement,fromUnit,toUnit):
    if fromUnit =="F":
        if toUnit=="C":
            return (measurement +32)* 5/9
        elif toUnit =="K":
            return (measurement +459.67)*5/9
    elif fromUnit == "C":
        if toUnit == "F":
            return  measurement *9/5 +32
        elif toUnit =="K":
            return  measurement - 273.15
        elif toUnit =="F":
            return  measurement *9/5 +273.15

def person(name,age,gender="Unknow"):
    print(name,age,gender)

print("sung",23,"None")





