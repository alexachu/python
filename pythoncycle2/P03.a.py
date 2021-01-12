#Positive list of numbers from a given list of integers
list=[10,-7,15,-20,40,-6,9]
pnum=[num for num in list if num >=0]
print("positive numbers are:", *pnum)
