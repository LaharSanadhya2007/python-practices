s1="make a lot of money"
s2="buy now"
s3="subscribe this"
s4="click this"
m=input("enter the msg:")
if(s1 in m or s2 in m or s3 in m or s4 in m):
    print("spam detected")
else:
    print("no spam detected")
