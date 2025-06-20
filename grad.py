physics=int(input("enter the marks"))
chemistry=int(input("enter the marks"))
bio=int(input("enter the marks"))
maths=int(input("enter the marks"))
computer=int(input("enter the marks"))
total=500
percentage=(physics+chemistry+bio+maths+computer)/total*100
if(percentage>=90):
    print("grade A")
elif(percentage>=80):
    print("grade B")
elif(percentage>=70):
    print("grade C")
elif(percentage>=60):
    print("grade D")
elif(percentage>=40):
    print("grade E")
elif(percentage==40):
    print("grade F")
else:
    print("fail")