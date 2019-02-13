a=str(input("enter ypur string"))
DIGITS=0
LETTERS=0
for i in a:
    if(i.isdigit()):
        DIGITS+=1
    else:
        LETTERS+=1

print("DIGITS :",DIGITS)
print("LETTERS :",LETTERS)
