a=str(input("enter your string"))
b=[]
for i in a:

    if(i not in b):
        print(i,a.count(i,0,len(a)))
    b.append(i)


