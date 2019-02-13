import numpy as np

arr=np.arange(16)
brr=arr.reshape((2,2,2,2))

k=np.sum(brr,axis=(2))
q=np.sum(brr,axis=(3))
print("K :",k)
print("Q :",q)
print("K+Q  : ",k+q)