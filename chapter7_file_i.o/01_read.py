f=open("file.txt")
c=f.read()
if ("twinkle" in c):
    print("twinkle present in file")
else:
    print("not present")
f.close()