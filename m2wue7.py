a=[12,24,35,24,88,120,155,88,120,155]

for i in a:
    if(a.count(i)>1):
        a.remove(i)

for i in a:
    print(i)