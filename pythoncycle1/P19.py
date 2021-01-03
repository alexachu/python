#program to reverse a number
a=int(input("Enter the number:"))
reverse=0
while a>0:
    reminder=a%10
    reverse=(reverse*10)+reminder
    a//=10
print("The reverse of a number is:",reverse)
