unit=int(input("enter the unit"))
surcharge=0.2
first50= 0.50/unit
total=unit+first50
if(first50<=50):
    totalbill=total+surcharge
    print("electric bill",totalbill)
else:
    print("not define")  
for_next100=0.75/unit  
if(for_next100==100):
    totalbill=total+surcharge
    print("electric bill",totalbill)
else:
    print("not define") 
next100=1.20/unit 
if(next100>=100):
    totalbill=total+surcharge
    print("electric bill",totalbill)
else:
    print("not define")    

