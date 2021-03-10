class Time1:
    def __init__(self, hour,minute,second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __add__(self, other):
        return self.hour + other.hour, self.minute + other.minute, self.second + other.second
class Time2:
    def __init__(self,hour,minute,second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __add__(self, other):
        return self.__hour + other.__hour, self.__minute + other.__minute, self.__second + other.__second
print("Time 1")
a=int(input("Enter the hour:"))
b= int(input("Enter the minute:"))
c= int(input("Enter the second:"))
print("Time 1 :-", a, ":", b, ":", c)

print("Time 2")
d=int(input("Enter the hour:"))
e= int(input("Enter the minute:"))
f= int(input("Enter the second:"))
print("Time 2 :-", d, ":", e, ":", f)

g=a+d
h=b+e
i=c+f
print("Sum of the times :-", g, ":", h, ":", i)