#Write a lamda functions find the area of a square,rectangle and triangle
#square:
a=int(input("Enter the width:"))
x=lambda b: b*b
print("Area of square:")
print(x(a))
#rectangle:
a=int(input("Enter the length:"))
b=int(input("Enter the width:"))
x=lambda a,b: a*b
print("Area of rectangle:")
print(x(a,b))
#triangle:
a=int(input("Enter the length:"))
b=int(input("Enter the width:"))
x=lambda a,b: 0.5*a*b
print("Area of triangle:")
print(x(a,b))

