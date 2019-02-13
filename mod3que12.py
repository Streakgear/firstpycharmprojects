q=str(input())
set={''}
k=q.split()
for i in k:
    set.add(i)
set=list(set)
set.sort()

for i in set:
    if(i!=" "):
        print(i," ",end='')