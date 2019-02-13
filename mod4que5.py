import numpy as np

list=[0, 5, 4, 0, 4, 4, 3, 0, 0, 5, 2, 1, 1, 9]
list.sort()
arr=np.array(list)
k=(max(arr))


arr_cpy=np.zeros(k+1)

for i in range(len(arr)):
    arr_cpy[arr[i]]+=1
print(arr_cpy)
