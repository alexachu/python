#Program to check whether the given number is palindrome or not
a=int(input("Enter the number:"))
temp=a
rev=0
while a > 0:
    d=a%10
    rev=rev*10+d
    a//=10
if temp==rev:
    print("The given number is Palindrome")
else:
    print("The given number is not palindrome")
