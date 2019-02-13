import numpy as np

arr=np.random.randint(100000,size=(3,3))
k=np.sort(arr,axis=0)
print(k)
