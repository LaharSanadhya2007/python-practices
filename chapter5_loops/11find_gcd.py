a=int(input("enter 1st num: "))
b=int(input("enter 2nd num: "))
for i in range(min(a,b),0,-1):
    if(a%i==0 and b%i==0):
        print("gcd:",i)
        break