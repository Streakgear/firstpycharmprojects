from math import sqrt
q=int(input("ENTER NUMBER OF INPUTS"))
list=[]
for i in range(q):
    q1=int(input())
    list.append(q1)
C=50
H=30

for i in list:
    D=sqrt(((2 * C * i)/H))
    print(round(D))