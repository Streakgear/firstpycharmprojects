
import random


res = [random.randrange(1, 10000, 1) for i in range(1000)]
b=[]
for i in res:
    if(i%5==0 or i%7==0):
        continue
    else:
        b.append(i)
for i  in range(0,5):
    print(b[i])