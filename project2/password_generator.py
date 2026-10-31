import random
characters= "abcdefghijklmnopqrstuvwxyz0123456789"
password=""
for i in range (8):
    password+=random.choice(characters)
print("generated password: ",password)