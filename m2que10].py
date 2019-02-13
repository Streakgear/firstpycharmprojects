a=[12,24,35,70,88,120,155]
b=[]

for i in a:
    if(i%5==0 or i%7==0):
        continue

    else:
        b.append(i)


print(b)