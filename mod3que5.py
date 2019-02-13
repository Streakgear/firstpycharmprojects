print("welcome to axis bank  ")
a=int(input("ENTER YOUR PIN  "))
dep=int(input("ENTER YOU INTIAL AMOUNT  "))
def axis(a,dep):

    while(1>0):

        print("ENTER 1 TO CASH DEPOSIT  ")
        print("ENTER 2 TO WITHDRAWL   ")
        print("ENTER 3 TO CHANGE PIN  ")
        print("ENTER 4 TO DISPLAY YOUR BALANCE")
        print("ENTER 5 TO EXIT BANK")

        x=int(input())
        if(x==1):
            k=int(input("ENTER AMOUNT TO DEPOSIT  "))
            dep=dep+k
        elif x==2:
            k1=int(input("ENTER YOUR AMOUNT TO WITHDRAW   "))
            if(k1>dep):
                print("AMOUNT GREATER THAN DEPOSIT  ")
            else:
                dep=dep-k1
        elif x==3:
            p=int(input("ENTER YOUR OLD PIN  "))
            if(p!=a):
                print("PIN ENTERED IS INCOREECT  ")
            else:
                a=p
                print("PIN CHANGED!  ")
        elif x==4:
            print("YOUR CURRENT BALANCE IS",)
            print(dep)
        elif x==5:
            print("THANKYOU FOR USING AXIS BANK")
            break

print("ENTER 1 TO ENTER BANK  ")
a=int(input())
if(a==1):
    axis(a,dep)
else:
    print("THANKYOU")