#Vending Machine
rupees=int(input("enter rupees:"))
if rupees>=10 and rupees<=20:
    print('candy')
elif rupees>=20 and rupees<=30:
    print("pastry")
elif rupees>=30 and rupees<=40:
    print("cold drink")
elif rupees>=40 and rupees<=60:
    print("choclate")
else:
    print("no item")