#program to find LCM of two numbers
def compute_lcm(x,y):
    if x>y:
        greater=x
    else:
        greater=y
    while(True):
        if((greater%x==0)and(greater%y==0)):
            lcm=greater
            break
        greater+=1
    return lcm
n1=int(input("Enter the frist number:"))
n2=int(input("Enter the second number:"))
print("The L.C.M is",compute_lcm(n1,n2))
