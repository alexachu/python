#Program to find largest among three numbers
a=int(input("Enter the first number:"))
b=int(input("Enter the second numer:"))
c=int(input("Enter the third number:"))
if a>b:
    if a>c:
        print("The largest is:", a)
    else:
        print("The largest is:", c)
elif b>c:
    print("The largest is:", b)
else:
    print("The largest is:",c)
    
    
