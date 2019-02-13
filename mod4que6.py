import numpy as np

list= [[0, 1, 2], [ 3, 4, 5], [ 6, 7,8],[ 9, 10, 11]]
index=[]
arr=np.array(list)
arr1=arr.ravel()

for i in range(len(arr1)):
    if arr1[i]>5:
        index.append(i)

new = np.delete(arr1,index )


arr1=new.reshape([2,3])
print(arr1)