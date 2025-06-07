amount=int(input("enter the amount"))
note500=amount//500
if(amount>=500):
     amount%=500
     print("note of 500",note500)
else:
    print ("note of 500=0")
note200=amount//200
if(amount>=200):
    amount%=200
    print("note of 200",note200)
else:
    print("note of 200=0")
note100=amount//100
if(amount>=100):
    amount%=100
    print("note of 100",note100)
else:
    print("note of 100=0")
note50=amount//50
if(amount>=50):
    amount%=50
    print("note of 50",note50)
else:
    print("note of 50=0")
note20=amount//20
if (amount>=20):
    amount%=20
    print("note of 20",note20)
else:
    print("note of 20=0")
note10=amount//10
if (amount>=10):
    amount%=10
    print("note of 10",note10)
else:
    print("note of 10=0")
