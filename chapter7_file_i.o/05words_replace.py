awords=["donkey","bad","stupid","fool"]
with open("words.txt","r") as f:
    content=f.read()
    for word in awords:
     content=content.replace(word,"#"*len(word))
with open("words.txt","w") as f:
    f.write(content)