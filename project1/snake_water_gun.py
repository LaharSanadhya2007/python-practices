import random
your_choice=input("enter your choice: ")
computer_choice=random.choice([1,-1,0])
your_dic={"s":1,"w":-1,"g":0}
rev_dic={1:"snake",-1:"water",0:"gun"}
you=your_dic[your_choice]
print(f"your_choice is {rev_dic[you]} \ncomputer choice is {rev_dic[computer_choice]}")
if(computer_choice==you):
    print("it's a draw.Try again.")
else:
    if(computer_choice==1 and you==-1):
        print("computer wins")
    elif(computer_choice==1 and you==0):
        print("you win")
    elif(computer_choice==-1 and you==1):
        print("you win")
    elif(computer_choice==-1 and you==0):
        print("computer wins")
    elif(computer_choice==0 and you==1):
        print("computer wins")
    elif(computer_choice==0 and you==-1):
        print("you win")
    else:
        print("something went wrong.try again later.")
