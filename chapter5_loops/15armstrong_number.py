n=int(input("enter num: "))
temp=n
rev=0
count=0
while(n>0):
    digit=n%10
    n=n//10
    count+=1
n=temp
while(n>0):
    digit=n%10
    n=n//10
    rev+=digit**count
if(rev==temp):
    print("armstrong")
else:
    print("not armstrong")
