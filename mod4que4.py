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
pwomen=0
pmen=0
l4.remove("PhD")
l2.remove('Gender')

for i in l4:
    if int(i)==0:
        pwomen+=1
    elif int(i)==1:
        pmen+=1

print("TOTAL NO OF PHD HOLDERS ARE", pmen)