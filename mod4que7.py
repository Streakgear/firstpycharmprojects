import numpy as np


arr=np.empty((5))
k=np.empty((5))
for i in range(len(arr)):
    arr[i]=i
    k[i]=i
arr[:1]=np.nan
arr[3:4]=np.nan


print(arr)
print(k)
