list=[]

q=int(input(("enter how many elements you want to store")))

for i in range (q):
    k=str(input())
    list.append(k)
list.sort()
e=str(input(" enter the element you want to search "))
print(e in list)