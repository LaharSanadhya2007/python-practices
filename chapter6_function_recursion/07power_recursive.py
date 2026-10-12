def power(a,b):
    if(b==0):
        return 1
    else:
        return(a*power(a,b-1))
a=int(input("enter base: "))
b=int(input("enter exponent: "))
print("power is:",power(a,b))