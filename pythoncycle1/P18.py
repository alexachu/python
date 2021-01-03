#Program to count number of digit in an integer
a=int(input("Enter the number:"))
count=0
while a > 0:
    count+=1
    a //=10
print("The number of digit in the given number are:",count)
    
    
