def factorial(a):
    if(a==1):
        return a
    else:
        return a*factorial(a-1)


c=factorial(8)
print(c)