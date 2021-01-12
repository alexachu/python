#Square of N numbers
n=int(input("Enter the n :"))
def sq(n):
    l=[i*i for i in range(1,n+1)]
    return l
print (sq(n))
