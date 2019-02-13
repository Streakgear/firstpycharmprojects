n,m = map(int,input().strip().split(" "))

l1=[]
l3=[]
l2=[]


for i in range (n):
    for j in range(m):
        l1.append(i*j)
    l2=l1.copy()
    l3.append(l2)
    l1.clear()

print(l3)
