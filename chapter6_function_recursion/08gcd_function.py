def gcd(a,b):
    for i in range(min(a,b),0,-1):
        if(a%i==0 and b%i==0):
            print("gcd is: ",i)
            return i
a=int(input("enter num 1:"))
b=int(input("enter num 2: "))
print("gcd: ",gcd(a,b))
