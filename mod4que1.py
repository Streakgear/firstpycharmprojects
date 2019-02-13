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
        l1.append(row[0])
        l2.append(row[1])
        l3.append(row[2])
        l4.append(row[3])
        salary=np.array(l1)
        gender=np.array(l2)
        age=np.array(l3)
        phd=np.array(l4)


print(salary)
print(gender)
print(age)
print(phd)