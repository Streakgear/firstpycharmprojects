a=int(input("enter the number to calculate factors"))
k=0
for i in range(2,int(a)):
    if a%i==0:

        if i%2==0:

            print(i," even")
        else:
            print(i,"odd")
        a=a/i
        i=2
    else:
        continue