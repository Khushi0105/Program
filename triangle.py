a=int(input("enter the no"))
b=int(input("enter the no"))
c=int(input("enter th no"))
if (a==b==c):
    print("triangle is equivalent")
elif((a==b and b!=c) or (a!=b and b==c ) or (a==c and b!=c )  ):
     print("triangle is iso")
elif(a!=b!=c):
    print("triangle is scalen")
else:
    print("nothing")   