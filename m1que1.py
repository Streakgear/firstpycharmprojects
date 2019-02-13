a=list(input("enter the password "))
Digit,Upper,Lower,special=0,0,0,0
for i in a:
    if i.isdigit():
        Digit=1
    elif i.islower():
         Lower=1
    elif i.isupper():
        Upper=1
    elif i=='$' or i=='#' or i=='@':
        special=1

l=len(a)

if(6<=l<=12 and Digit==1 and Lower==1 and Upper ==1 and special==1):
    print("password is valid")
else:
    print("password is not valid")
