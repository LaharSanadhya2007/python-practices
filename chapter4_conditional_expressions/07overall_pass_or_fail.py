a=int(input("enter marks 1"))
b=int(input("enter marks 2"))
c=int(input("enter marks 3"))
total_per=((a+b+c)/300)*100
if(total_per>=40 and a>=33 and b>=33 and c>=33):
    print("pass",total_per)
else:
    print("fail",total_per)
