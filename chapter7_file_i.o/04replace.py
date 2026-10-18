word="donkey"
with open("donk.txt","r") as f:
    content=f.read()
contentN=content.replace(word,"######")
with open("donk.txt","w") as f:
    f.write(contentN)

