amount = int(input())
balance = float(input())
def atm(amount,balance):
    if(0<amount<=2000 and 0<=balance<=2000):
        if(amount%5 == 0 and amount < balance):
            print("%.2f" % (balance - (amount + 0.50)))
        elif(amount%5 != 0 and amount < balance):
            print("%.2f" % balance)
        else:
            print("%.2f" % balance)
atm(amount,balance)