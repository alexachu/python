#program find the power of a number
def power(base,exp):
        if exp == 1:
             return(base)
        if exp!=1:
             return(base*power(base,exp-1))
base=int(input("Enter the base value:"))
exp=int(input("Enter the expression value:"))
print("The power",power(base,exp))
     
