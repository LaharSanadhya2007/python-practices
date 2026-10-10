n=int(input("enter a num: "))
rev=0
while(n>0):
    digit=n%10
    n=n//10
    rev=rev*10+digit
print(rev)
