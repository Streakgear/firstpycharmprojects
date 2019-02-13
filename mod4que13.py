import numpy as np
l=[]
m=[]
arr=np.arange(16)
brr=arr.reshape(4,4)


arr=brr.copy()

brr[0]=arr[1]
brr[1]=arr[0]
print(brr)
