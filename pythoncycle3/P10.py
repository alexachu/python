#Generate all factors of a number
n=int(input("Enter the number:"))
print("Factors of ",n,"is:")
for i in range(1,n+1):
    if n%i==0:
        print(i)

