import  pandas
import numpy as np
import csv
l1=[]
l2=[]
l3=[]
l4=[]
with open('SalaryGender.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:

        l2.append(row[1])

        l4.append(row[3])
w=0
m=0
l4.remove("PhD")
l2.remove('Gender')
for i in range(len(l2)):
    if int(l2[i])==1:
        if int(l4[i])==1:
            m+=1

    elif int(l2[i])==0:
        if int(l4[i]) == 1:
            w+=1

print("MEN : ",m,"WOMEN :",w)