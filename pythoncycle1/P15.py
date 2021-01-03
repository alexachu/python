#Program to generate multiplication table 
a=int(input("Enter the range:"))
b=int(input("Enter the number in which multiplication table print:"))
for x in range(1,a+1):
    print(b,'x',x,'=',b*x)
