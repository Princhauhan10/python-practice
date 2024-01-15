# ATM  Simulator

print('''
----------------------------------------------------------------
|            ATM Simulator                                      |
|            1 Widthdraw amount                                 |
|            2 Deposit amount                                   |
|            3 Balance check                                    |
|            4 Pin Change                                       |
|            5 Transaction details                              |
-----------------------------------------------------------------''')
org_pin=1111
bal=200000
user=int(input('Enter your pin: '))
if user==org_pin:
    choice=int(input('Enter your choice: '))
    if choice==1:
        print('Processing, please wait.....')
        a_wd=int(input('Enter amount: '))
        if a_wd<=bal:
            print('Processing, please wait.....')
            bal-=a_wd
            print('Transaction successful')
        else:
            print('Insufficient amount')
    elif choice==2:
        print('Processing, please wait.....')
        a_dd=int(input('Enter amount: '))
        print('Processing, please wait.....')
        bal+=a_dd
        print('Transaction successful')
    elif choice==3:
        print('Your current balance is:', bal)
    elif choice==4:
        or_pin=int(input('Enter your pin: '))
        if or_pin==org_pin:
            new_pin=int(input('Enter your new pin: '))
            conf_pin=int(input('confirm your new  pin: '))
            if new_pin==conf_pin:
                org_pin=new_pin
                print('Pin changed successfully')
            else:
                print('Pin not matched')
        else:
            print('Invalid pin')
else:
    print('Invalid pin, try again later')