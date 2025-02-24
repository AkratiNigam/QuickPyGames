import random

computer = random.randint(1,100)
print("welcome to the game, guess the number:")


user = -1
tries = 0
while(user!= computer):
    tries += 1
    user = int(input("enter your guess between 1 and 100"))
    if(computer>user):
     print("guess a higher number")
    elif(computer<user):
     print("guess a lower number")
    else:
     print(f"congratulations your guess is right, you got {computer} in {tries} tries")