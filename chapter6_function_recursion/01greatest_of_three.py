def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
a=int(input("enter 1st num: "))
b=int(input("enter 2nd num: "))
c=int(input("enter 3rd num: "))
print("greatest number is:",greatest(a,b,c))