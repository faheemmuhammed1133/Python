import banca
a=banca.Atm()
bank={1:"Deposite",2:"Withdraw",3:"Checkbalance"}
print("____welcome____")
while True:
    print("\n",bank)
    op=int(input())
    if op==1:
        a.deposite()
    elif op ==2:
        a.withdrawal()
    elif op==3:
        a.balncecheck()
    else:
        print("invald choice!")
        break