a=int(input("enter your number"))
i=1.0
k=0.0


for i in range (1,a+1):
    k=k+(i/(i+1))
print(round(k,2))