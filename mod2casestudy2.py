import csv
set={''}
l=[]
m=[]
with open('bank-data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        set.add(row[1])
        l.append((row[0]))

set.remove('')
set.remove('services')
set=list(set)
for i in set:
    m.append(i.upper())

l.remove('age')
ma=max(l)
mi=min(l)
dict={'maximum':ma,'minimum':mi}

while(1>0):
    print("PRESS 1 TO CHECK PROFESSION")
    print("PRESS 2 TO EXIT ")
    key=int(input())
    if key==1:
        q=str(input("PLEASE ENTER THE PROFESSION  :"))
        q=q.upper()
        if q in m:
            print("ELIGIBLE FOR LOAN ")
            print("MAX AGE LIMIT IS ",dict['maximum']," MINIMUM AGE LIMIT IS ",dict['minimum'])
        else:
            print("NOT ELIGIBLE FOR LOAN  ")
    elif key==2:
        print("THANKYOU   ")
        break