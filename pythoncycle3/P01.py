#Find the factorial of a number
n=int(input("Enter the number:"))
fac=1
while(n>0):
    fac=fac*n
    n=n-1
print("Factorial is:",fac)
