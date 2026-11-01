a=float(input("enter 1st number: "))
b=float(input("enter 2nd number: "))
op=input("enter any operation +,-,*,/: ")
if op=='+':
    print(a+b)
elif op=='-':
    print(a-b)
elif op=='*':
    print(a*b)
elif op=='/':
    if b!=0:
        print(a/b)
    else:
        print("error: division by 0")
else:
    print("invalid opeeration")