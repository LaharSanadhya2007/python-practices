n=int(input("enter num: "))
p=n
rev=0
while(n>0):
    digit=n%10
    n=n//10
    rev=rev*10+digit
print(rev)
if(p==rev):
     print("palindrome")
else:
    print("palindrome not")
    