q=str(input())

k=q.split(",")
l=sorted(k)
# print(str(l))
count=0
for i in l:
    count+=1
m=0
for i in l:
    m+=1
    if(m!=2):
        print(i,end=',')
    elif(m==2):
        print(i,end='')

#should have used len but i am used to kinda c++ hehe sorry