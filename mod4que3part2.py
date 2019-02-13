import  pandas as pd
import numpy as np
import csv
l1=[]
l2=[]
l3=[]
l4=[]
with open('SalaryGender.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        l1.append(row[0])
        l2.append(row[1])
        l3.append(row[2])
        l4.append(row[3])
l4.remove("PhD")
l3.remove("Age")
a1=0
a2=0
a3=[]

a3=(l4)
size=len(l4)
x=0
while(x<size):
    if l4[x]=='0':
        l4.remove(l4[x])
        l3.remove(l3[x])
        x-=1
        size-=1
    x+=1



df=pd.DataFrame({'age':l3,
                 'Phd' :l4})
print(df)