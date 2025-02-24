import random

computer = random.choice([0,1,-1])
you = input("enter your choice")
youdict = {"rock":0, "paper":1, "scissor": -1}
reversedict = {0:"rock",1:"paper",-1:"scissor"}

player = youdict[you]
print(f"you chose {reversedict[player]}\nand computer chose {reversedict[computer]}")

if(player==computer):
    print("its a draw")
else:    
 if(player==0 and computer==1):
    print("you lose")
 elif(player==0 and computer==-1):
    print("you win!")
 elif(player==1 and computer==-1):
    print("you lose")
 elif(player==1 and computer==0):
    print("you win!")
 elif(player==-1 and computer==1):
    print("you win!")
 elif(player==-1 and computer==0):
    print("you lose")
 else:
     print("error")
    
