k=0
for i in range (1000,3000):
    a=str(i)
    for j in a:
        if(int(j)%2!=0):
            k=1
    if(k==0):
        print(i)
    else:
        k=0