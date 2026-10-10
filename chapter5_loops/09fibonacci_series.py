n=int(input("enter num: "))
fib1=0
fib2=1
for i in range(n):
    print(fib1)
    next=fib1+fib2
    fib1=fib2
    fib2=next
