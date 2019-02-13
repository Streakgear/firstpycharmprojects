q=str(input())

k=q.split(',')


for i in k:
    m=int(i,2)
    if(m%5==0):
        print(i)