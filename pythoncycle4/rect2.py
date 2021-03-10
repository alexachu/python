class Rectangle:
    def __init__(self ,width, length):
        self.__width = width
        self.__length = length
    def area(self):
        return self.__width * self.__length
print("Rectangle 1")
a=int(input("enter the length:"))
b= int(input("enter the width:"))
obj=Rectangle(a,b)

print("Area 1 = ",obj.area())
print("Rectangle 2")
a=int(input("enter the length:"))
b= int(input("enter the width:"))
ob=Rectangle(a,b)

print("Area 2= ",ob.area())
rec1 = obj.area()
rec2 = ob.area()
if(rec1>rec2):
    print("Area of Rectangle 1 is greater than Rectangle 2")
elif(rec1==rec2):
    print("Area of Rectangle 1 is equal to Rectangle 2")
else:
    print("Area of Rectangle 2 is greater than Rectangle 1")