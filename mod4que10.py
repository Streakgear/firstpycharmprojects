import numpy as np

arr=np.empty(11)

for i in range(len(arr)):
    arr[i]=i

arr[3:10]=np.nan
print(arr)