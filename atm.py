available_amount=int(input("enter the amount"))
withdraw_amount=int(input("enter the cash"))
bank_charge=0.50
withdraw=withdraw_amount+bank_charge
if(available_amount>=withdraw):
    if(withdraw_amount%5==0):
        availAmount = available_amount-withdraw
        print("Amount withdraw successfully, your available amount is:", availAmount)
    else:
        print("withdraw amount not divisible by 5")
else:
    print("ensufficint amount")