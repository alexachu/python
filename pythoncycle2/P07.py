#Enter 2 lists of integers,Check whether list are same length,list sums to same value,any value occur in both 
l1=[10,15,20]
l2=[4,8,16,32]
s1=len(l1)
s2=len(l2)
if s1==s2:
    print("The length of the two string are same")
else:
    print("The length of the two string are not same") 

x1=sum(l1)
print("The sum of l1:",x1)
x2=sum(l2)
print("The sum of l2:",x2)
if x1==x2:
    print("The sum of the values are same")
else:
    print("The sum of the values are not same")
    
a=set(l1)
b=set(l2)
if(a&b):
    print(a&b)
else:
    print("No element is common")
