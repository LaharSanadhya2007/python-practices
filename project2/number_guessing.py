import random
number=random.randint(1,10)
guess=int(input("enter a number from 1 to 10: "))
if guess==number:
    print("you won")
else:
    print("u enter wrong number,the number was",number)