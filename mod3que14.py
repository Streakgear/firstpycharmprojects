q=str(input())
u=0
l=0
for i in q:
    if i.isupper():
        u+=1
    elif i.islower():
        l+=1
    else:
        continue
print("UPPER CASE",u)
print("LOWER CASE",l)
